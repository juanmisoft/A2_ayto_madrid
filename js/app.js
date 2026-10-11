const BANK = window.BANK;
const STORE = "a2madrid-tic-v1";
const SESSION = "a2madrid-tic-exam";
const LETTERS = ["A", "B", "C"];

const state = {
  route: "/",
  stats: loadStats(),
  exam: loadExam(),
  setup: {
    count: 20,
    timer: false,
    study: true,
    topics: [],
  },
  practicalFilter: "todos",
  revealed: {},
  timerId: null,
};

const main = document.querySelector("#contenido");
const nav = document.querySelector("#site-nav");

document.querySelector(".nav-toggle").addEventListener("click", (event) => {
  const open = nav.classList.toggle("open");
  event.currentTarget.setAttribute("aria-expanded", String(open));
});
nav.addEventListener("click", () => {
  nav.classList.remove("open");
  document.querySelector(".nav-toggle").setAttribute("aria-expanded", "false");
});
window.addEventListener("hashchange", render);
document.addEventListener("keydown", onKey);

function loadStats() {
  try {
    return JSON.parse(localStorage.getItem(STORE)) || { questions: {}, exams: [] };
  } catch {
    return { questions: {}, exams: [] };
  }
}

function saveStats() {
  localStorage.setItem(STORE, JSON.stringify(state.stats));
}

function loadExam() {
  try {
    return JSON.parse(sessionStorage.getItem(SESSION));
  } catch {
    return null;
  }
}

function saveExam() {
  if (state.exam) sessionStorage.setItem(SESSION, JSON.stringify(state.exam));
  else sessionStorage.removeItem(SESSION);
}

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[char]));
}

function inline(value) {
  return esc(value).replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
}

function markdown(source) {
  const lines = String(source || "").replace(/\r/g, "").split("\n");
  let html = "";
  let list = false;
  const close = () => {
    if (list) {
      html += "</ul>";
      list = false;
    }
  };
  for (const line of lines) {
    if (line.startsWith("## ")) {
      close();
      html += `<h3>${esc(line.slice(3))}</h3>`;
    } else if (line.startsWith("- ")) {
      if (!list) {
        html += "<ul>";
        list = true;
      }
      html += `<li>${inline(line.slice(2))}</li>`;
    } else if (!line.trim()) {
      close();
    } else {
      close();
      html += `<p>${inline(line)}</p>`;
    }
  }
  close();
  return html;
}

function shuffle(list) {
  const copy = [...list];
  for (let index = copy.length - 1; index > 0; index -= 1) {
    const swap = Math.floor(Math.random() * (index + 1));
    [copy[index], copy[swap]] = [copy[swap], copy[index]];
  }
  return copy;
}

function topicTitle(id) {
  if (!id) return "Sin tema asignado";
  const topic = BANK.syllabus.find((item) => item.id === id);
  return topic ? `Tema ${topic.id}. ${topic.title}` : `Tema ${id}`;
}

function topicShort(id) {
  if (!id) return "Sin tema";
  return `T${id}`;
}

function parseRoute() {
  const raw = decodeURIComponent(location.hash.replace(/^#/, "") || "/");
  const [path, query = ""] = raw.split("?");
  const params = new URLSearchParams(query);
  return { path: path || "/", params };
}

function go(path) {
  location.hash = path;
}

function render() {
  const { path } = parseRoute();
  state.route = path;
  document.querySelectorAll(".site-nav a").forEach((link) => {
    const route = link.dataset.route;
    const current = route === "/" ? path === "/" : path.startsWith(route);
    link.toggleAttribute("aria-current", current && route !== "/examen");
    if (route === "/" && path !== "/") link.removeAttribute("aria-current");
  });
  clearInterval(state.timerId);
  if (!BANK) {
    main.innerHTML = "<p>No se ha cargado el banco de preguntas.</p>";
    return;
  }
  if (path === "/") main.innerHTML = viewHome();
  else if (path === "/teoria") main.innerHTML = viewTheory();
  else if (path === "/examen") main.innerHTML = viewExam();
  else if (path === "/resultado") main.innerHTML = viewResult();
  else if (path === "/revision") main.innerHTML = viewReview();
  else if (path === "/practica") main.innerHTML = viewPracticalList();
  else if (path.startsWith("/practica/")) main.innerHTML = viewPractical(path.split("/")[2]);
  else if (path === "/progreso") main.innerHTML = viewProgress();
  else if (path === "/metodo") main.innerHTML = viewMethod();
  else main.innerHTML = viewHome();
  bind();
  if (path === "/examen" && state.exam && !state.exam.submitted && state.exam.endsAt) startTimer();
}

function lastExam() {
  return state.stats.exams[0];
}

function failedIds() {
  return Object.entries(state.stats.questions)
    .filter(([, record]) => record.bad > record.ok)
    .map(([id]) => id);
}

function viewHome() {
  const last = lastExam();
  const total = BANK.questions.length;
  const official = BANK.questions.filter((q) => q.origin === "examen-oficial").length;
  return `
    <section class="hero">
      <div>
        <p class="kicker">Oposición A2 · Bases de 2026</p>
        <h1>Prepara el primer ejercicio y los supuestos con el baremo oficial.</h1>
        <p class="lede">Cuestionario de 100 preguntas y 7 de reserva, tres opciones y penalización de un tercio. Los supuestos se contestan con el criterio de las bases: conocimiento y análisis, a partes iguales.</p>
      </div>
      <aside class="score-pill">
        ${last ? `<span>Último simulacro o entrenamiento</span><b class="${last.score >= 5 ? "pass" : "fail"}">${last.score.toFixed(2)}</b><span>sobre 10 · ${formatDate(last.date)}</span>` : `<span>Aún no hay nota guardada en este navegador</span><b>—</b><span>${total} preguntas en el banco, ${official} de exámenes anteriores</span>`}
      </aside>
    </section>
    <div class="grid-2">
      <article class="module">
        <p class="kicker">Módulo 1</p>
        <h2>Parte teórica</h2>
        <p>Simulacro con la estructura de las bases, entrenamiento por temas y repaso de fallos. Ninguna pregunta se repite dentro del mismo ejercicio y el sorteo reparte temas del programa.</p>
        <div class="actions">
          <button class="btn" type="button" data-action="simulacro">Simulacro oficial</button>
          <a class="btn secondary" href="#/teoria">Configurar entrenamiento</a>
        </div>
      </article>
      <article class="module">
        <p class="kicker">Módulo 2</p>
        <h2>Ejercicios prácticos</h2>
        <p>Enunciados de las pruebas anteriores y supuestos de refuerzo tomados de la sede, los datos abiertos y la organización municipal. Cada uno incluye una contestación alineada con el criterio de corrección.</p>
        <div class="actions">
          <a class="btn" href="#/practica">Ver supuestos</a>
          <a class="btn secondary" href="#/metodo">Cómo sumar décimas</a>
        </div>
      </article>
    </div>
    <section class="grid-3 panel">
      <article class="card"><h3>No dejes en blanco por sistema</h3><p>Con tres opciones y una penalización de 1/3, responder al azar tiene esperanza positiva. Si descartas una opción, compensa aún más marcar.</p></article>
      <article class="card"><h3>Cubre el programa, no solo el último examen</h3><p>Las bases piden preguntas de todos los temas. El simulacro reparte antes de rellenar, para que un tema no desaparezca del cuaderno.</p></article>
      <article class="card"><h3>El 5 es el mínimo, no la nota de corte</h3><p>Hay que sacar 5,00 en cada ejercicio. El tribunal puede exigir un nivel mayor para que ese 5 empiece más arriba.</p></article>
    </section>`;
}

function viewTheory() {
  const fails = failedIds().length;
  const selected = new Set(state.setup.topics);
  const chips = BANK.syllabus.map((topic) => `
    <button type="button" class="chip" data-topic="${topic.id}" aria-pressed="${selected.has(topic.id)}">
      ${topic.group === "I" ? "I" : "II"} · ${topic.id}
    </button>`).join("");
  return `
    <p class="kicker">Parte teórica</p>
    <h1>Elige el tipo de test.</h1>
    <div class="grid-2 panel">
      <article class="card">
        <h2>Simulacro oficial</h2>
        <p>100 preguntas puntuables y 7 de reserva. Tiempo: 107 minutos. La nota sale solo de las 100 primeras, como en el ejercicio.</p>
        <button class="btn" type="button" data-action="simulacro">Empezar simulacro</button>
      </article>
      <article class="card">
        <h2>Entrenamiento</h2>
        <label>Número de preguntas
          <select id="count">
            ${[10, 20, 30, 50].map((n) => `<option ${state.setup.count === n ? "selected" : ""}>${n}</option>`).join("")}
          </select>
        </label>
        <p><label><input id="with-timer" type="checkbox" ${state.setup.timer ? "checked" : ""}> Cronómetro a un minuto por pregunta</label></p>
        <p><label><input id="study-mode" type="checkbox" ${state.setup.study ? "checked" : ""}> Corregir al responder</label></p>
        <div class="actions">
          <button class="btn" type="button" data-action="train">Empezar entrenamiento</button>
          <button class="btn secondary" type="button" data-action="fails" ${fails ? "" : "disabled"}>Repasar fallos (${fails})</button>
        </div>
      </article>
    </div>
    <section class="card panel">
      <h2>Temas</h2>
      <p class="help">Si no marcas ninguno, entran todos. El grupo I son los temas 1 a 14 y el II, del 15 al 69.</p>
      <div class="actions">
        <button class="btn secondary" type="button" data-action="group" data-group="I">Grupo I</button>
        <button class="btn secondary" type="button" data-action="group" data-group="II">Grupo II</button>
        <button class="btn ghost" type="button" data-action="clear-topics">Quitar selección</button>
      </div>
      <div class="chips" style="margin-top:0.8rem">${chips}</div>
    </section>`;
}

function viewExam() {
  const exam = state.exam;
  if (!exam || exam.submitted) {
    return `<h1>No hay un ejercicio en curso.</h1><p><a class="btn" href="#/teoria">Ir a teoría</a></p>`;
  }
  const question = exam.questions[exam.index];
  const totalMain = exam.questions.filter((item) => !item.reserve).length;
  const label = question.reserve ? "Reserva" : `Pregunta ${exam.index + 1} de ${exam.questions.length}`;
  const answer = exam.answers[question.id];
  const locked = exam.study && answer !== undefined && answer !== null;
  const options = question.choices.map((choice, index) => {
    let cls = "option";
    if (answer === index) cls += " selected";
    if (locked && index === question.answer) cls += " good";
    if (locked && answer === index && index !== question.answer) cls += " bad";
    return `<button type="button" class="${cls}" role="radio" aria-checked="${answer === index}" data-choice="${index}">
      <span class="letter">${LETTERS[index]}</span><span>${esc(choice)}</span>
    </button>`;
  }).join("");
  const explanation = locked ? `<div class="callout"><strong>${answer === question.answer ? "Correcta." : "Incorrecta."}</strong> ${esc(question.explanation || "")}</div>` : "";
  const map = exam.questions.map((item, index) => {
    const marked = exam.answers[item.id];
    const classes = [
      index === exam.index ? "current" : "",
      marked === null ? "blanked" : "",
      Number.isInteger(marked) ? "answered" : "",
      item.reserve ? "reserve" : "",
    ].filter(Boolean).join(" ");
    return `<button type="button" class="${classes}" data-jump="${index}" aria-label="Ir a la pregunta ${index + 1}">${index + 1}</button>`;
  }).join("");
  const remaining = exam.endsAt ? Math.max(0, exam.endsAt - Date.now()) : null;
  return `
    <div class="exam-top">
      <div>
        <p class="kicker">${esc(exam.title)}</p>
        <strong>${label}</strong>
      </div>
      <div class="timer ${remaining !== null && remaining < 10 * 60 * 1000 ? "warning" : ""}" id="timer">${remaining === null ? "Sin tiempo" : formatClock(remaining)}</div>
    </div>
    <div class="progress" aria-hidden="true"><span style="width:${((exam.index + 1) / exam.questions.length) * 100}%"></span></div>
    <article class="card question-card">
      <div class="meta">
        <span>${esc(topicShort(question.topic))}</span>
        ${question.reserve ? '<span class="badge">No puntúa salvo anulación</span>' : `<span>Puntuables: ${totalMain}</span>`}
        <span>${esc(question.source)}</span>
      </div>
      <h2 class="stem">${esc(question.stem)}</h2>
      <div class="options" role="radiogroup" aria-label="Opciones de respuesta">${options}</div>
      ${explanation}
    </article>
    <div class="exam-nav">
      <button class="btn secondary" type="button" data-action="prev" ${exam.index === 0 ? "disabled" : ""}>Anterior</button>
      <button class="btn secondary" type="button" data-action="blank">En blanco</button>
      <button class="btn secondary" type="button" data-action="next">${exam.index === exam.questions.length - 1 ? "Revisar" : "Siguiente"}</button>
      <button class="btn" type="button" data-action="finish">Entregar</button>
    </div>
    <div class="map" aria-label="Mapa de preguntas">${map}</div>
    <p class="help">Teclas 1, 2 y 3 para responder. Las casillas discontinuas son la reserva.</p>`;
}

function viewResult() {
  const exam = state.exam;
  if (!exam || !exam.submitted || !exam.grade) {
    return `<h1>Todavía no hay una entrega.</h1><p><a href="#/teoria">Volver a teoría</a></p>`;
  }
  const grade = exam.grade;
  const passed = grade.score >= BANK.meta.pass;
  const topics = Object.entries(grade.byTopic)
    .map(([id, row]) => ({ id: Number(id), ...row, rate: row.total ? row.correct / row.total : 0 }))
    .sort((a, b) => a.rate - b.rate);
  const weak = topics.filter((topic) => topic.total >= 1 && topic.rate < 0.6).slice(0, 5);
  return `
    <p class="kicker">${esc(exam.title)}</p>
    <h1 class="${passed ? "pass" : "fail"}">${passed ? "Por encima del mínimo" : "Por debajo del mínimo"}</h1>
    <p class="big-score ${passed ? "pass" : "fail"}">${grade.score.toFixed(2)}</p>
    <p>Escala de 0 a 10. Para superar el ejercicio las bases exigen al menos 5,00. ${passed ? "Este cuaderno supera ese mínimo." : "Con esta plantilla el ejercicio no llega al 5,00."}</p>
    <div class="stats">
      <div class="stat"><b>${grade.pctCorrect.toFixed(1)}%</b><span>Acertadas · ${grade.correct}</span></div>
      <div class="stat"><b>${grade.pctWrong.toFixed(1)}%</b><span>Falladas · ${grade.wrong}</span></div>
      <div class="stat"><b>${grade.pctBlank.toFixed(1)}%</b><span>En blanco · ${grade.blank}</span></div>
      <div class="stat"><b>${grade.net.toFixed(2)}</b><span>Netas sobre ${grade.n}</span></div>
    </div>
    <p class="formula">Nota = máximo(0, (aciertos − errores / 3) / ${grade.n} × 10), redondeada al segundo decimal.${exam.questions.some((q) => q.reserve) ? ` Las ${exam.questions.filter((q) => q.reserve).length} de reserva no entran en esta nota.` : ""}</p>
    <div class="two-col panel">
      <article class="card">
        <h2>Dónde se van los puntos</h2>
        <div class="bars">
          ${topics.slice(0, 8).map((topic) => `
            <div class="bar-row">
              <span>${esc(topicShort(topic.id))}</span>
              <div class="bar"><span style="width:${topic.rate * 100}%"></span></div>
              <span>${topic.correct}/${topic.total}</span>
            </div>`).join("")}
        </div>
      </article>
      <article class="card">
        <h2>Siguiente sesión</h2>
        ${weak.length ? `<p>Vuelve primero a estos temas:</p><ul>${weak.map((topic) => `<li>${esc(topicTitle(topic.id))}</li>`).join("")}</ul>` : "<p>No hay un tema claramente por debajo del 60 %. Sube el volumen de simulacros para afinar.</p>"}
        <div class="actions">
          <a class="btn" href="#/revision">Revisar el cuaderno</a>
          <button class="btn secondary" type="button" data-action="retry-weak" ${weak.length ? "" : "disabled"}>Entrenar los flojos</button>
        </div>
      </article>
    </div>`;
}

function viewReview() {
  const exam = state.exam;
  if (!exam || !exam.submitted) return `<h1>No hay un cuaderno para revisar.</h1>`;
  const rows = exam.questions.filter((q) => !q.reserve).map((question, index) => {
    const answer = exam.answers[question.id];
    const ok = answer === question.answer;
    const status = answer === null || answer === undefined ? "En blanco" : ok ? "Acierto" : "Fallo";
    return `<article class="card">
      <p class="meta">${index + 1} · ${esc(status)} · ${esc(topicShort(question.topic))}</p>
      <h3>${esc(question.stem)}</h3>
      <p><strong>Tu respuesta:</strong> ${answer === null || answer === undefined ? "en blanco" : `${LETTERS[answer]}. ${esc(question.choices[answer])}`}</p>
      <p><strong>Plantilla:</strong> ${LETTERS[question.answer]}. ${esc(question.choices[question.answer])}</p>
      <p>${esc(question.explanation || "")}</p>
    </article>`;
  }).join("");
  return `<p class="kicker">Revisión</p><h1>Preguntas puntuables</h1><div class="list">${rows}</div>`;
}

function viewPracticalList() {
  const filter = state.practicalFilter;
  const items = BANK.practicals.filter((item) => {
    if (filter === "oficial") return item.origin === "oficial";
    if (filter === "refuerzo") return item.origin !== "oficial";
    if (filter === "supuesto") return item.kind === "supuesto";
    if (filter === "composicion") return item.kind === "composicion";
    return true;
  });
  const button = (id, label) => `<button type="button" class="chip" data-filter="${id}" aria-pressed="${filter === id}">${label}</button>`;
  return `
    <p class="kicker">Parte práctica</p>
    <h1>Enunciado y contestación.</h1>
    <p class="lede">El segundo ejercicio de las bases tiene dos partes de dos horas: un tema de composición y un supuesto. Aquí están los supuestos de las pruebas guardadas en el proyecto y otros construidos con fuentes abiertas del propio Ayuntamiento.</p>
    <div class="filters">
      ${button("todos", "Todos")}
      ${button("oficial", "De examen")}
      ${button("refuerzo", "Refuerzo")}
      ${button("supuesto", "Supuestos")}
      ${button("composicion", "Composición")}
    </div>
    <div class="list">
      ${items.map((item) => `
        <a class="card" href="#/practica/${esc(item.id)}">
          <span class="tag">${item.origin === "oficial" ? "Examen oficial" : "Refuerzo"} · ${item.kind === "composicion" ? "Composición" : "Supuesto"} · ${item.minutes} min</span>
          <h2>${esc(item.title)}</h2>
          <p>${esc(item.source)}</p>
        </a>`).join("")}
    </div>`;
}

function viewPractical(id) {
  const item = BANK.practicals.find((entry) => entry.id === id);
  if (!item) return `<h1>No está ese supuesto.</h1>`;
  const open = state.revealed[id];
  return `
    <p class="kicker"><a href="#/practica">Volver a la lista</a></p>
    <h1>${esc(item.title)}</h1>
    <p class="help">${esc(item.source)}${item.pdf ? ` · Cuaderno: ${esc(item.pdf)}` : ""}</p>
    <div class="callout"><strong>Criterio de las bases.</strong> ${esc(item.rubric)} Tiempo de referencia: ${item.minutes} minutos. Temas: ${item.topics.map(topicShort).join(", ")}.</div>
    <article class="card prose">${markdown(item.statement)}</article>
    <div class="actions panel">
      <button class="btn" type="button" data-action="reveal" data-id="${esc(item.id)}">${open ? "Ocultar contestación" : "Ver una contestación posible"}</button>
    </div>
    ${open ? `<article class="card prose panel"><h2>Contestación de trabajo</h2>${markdown(item.answer)}
      <h3>Lista antes de pasar a limpio</h3>
      <ul>
        <li>¿Cada apartado responde a lo que pide el enunciado, o a un tema parecido?</li>
        <li>¿Hay un dibujo o un esquema donde el apartado lo pide?</li>
        <li>¿Las suposiciones están escritas y justificadas?</li>
        <li>¿El cierre distingue lo organizativo de lo técnico?</li>
      </ul>
    </article>` : `<p class="help panel">Escribe tu esquema antes de abrir la contestación. Si la lees primero, el ejercicio deja de entrenar el análisis.</p>`}`;
}

function viewProgress() {
  const cells = BANK.syllabus.map((topic) => {
    const rows = Object.entries(state.stats.questions).filter(([id]) => {
      const question = BANK.questions.find((item) => item.id === id);
      return question && question.topic === topic.id;
    });
    let ok = 0;
    let bad = 0;
    rows.forEach(([, record]) => {
      ok += record.ok;
      bad += record.bad;
    });
    const attempts = ok + bad;
    const rate = attempts ? ok / attempts : null;
    const cls = rate === null ? "none" : rate >= 0.75 ? "good" : rate >= 0.5 ? "mid" : "bad";
    return `<a class="${cls}" href="#/teoria" data-focus-topic="${topic.id}"><strong>${topic.id}</strong><br>${attempts ? `${Math.round(rate * 100)}% en ${attempts}` : "Sin datos"}</a>`;
  }).join("");
  const history = state.stats.exams.slice(0, 12);
  return `
    <p class="kicker">Progreso en este navegador</p>
    <h1>Mapa del temario.</h1>
    <p class="help">Verde a partir del 75 % de aciertos, crema entre 50 y 75, rojo por debajo. El porcentaje sale de los ejercicios ya entregados.</p>
    <div class="heat">${cells}</div>
    <section class="card panel">
      <h2>Entregas</h2>
      ${history.length ? `<table class="history"><thead><tr><th>Fecha</th><th>Modo</th><th>Nota</th><th>Aciertos</th><th>Fallos</th><th>Blancos</th></tr></thead><tbody>
        ${history.map((exam) => `<tr><td>${formatDate(exam.date)}</td><td>${esc(exam.mode)}</td><td>${exam.score.toFixed(2)}</td><td>${exam.correct}</td><td>${exam.wrong}</td><td>${exam.blank}</td></tr>`).join("")}
      </tbody></table>` : "<p>Cuando entregues el primer test aparecerá aquí.</p>"}
    </section>`;
}

function viewMethod() {
  return `
    <p class="kicker">Método</p>
    <h1>Cómo se traduce el baremo a una nota.</h1>
    <article class="card prose">
      <h3>Primer ejercicio</h3>
      <p>100 preguntas del programa, más 7 de reserva por si el tribunal anula alguna. Tiempo: 100 minutos más 7. Tres alternativas y una sola correcta. La reserva se contesta, pero esta aplicación no la suma a la nota.</p>
      <p class="formula">Netas = aciertos − (errores / 3)<br>Nota = netas / 100 × 10</p>
      <p>Lo no contestado, o marcado de más de una forma, vale cero. La nota se redondea al segundo decimal y no baja de cero. Con 50 aciertos y 50 blancos sale un 5,00. Si no dejas ninguna en blanco, necesitas 63 aciertos para no bajar de 5, porque 37 errores restan 12,33 netas.</p>
      <h3>Cuándo marcar</h3>
      <p>La penalización que deja el azar a cero sería 1/2, porque hay dos distractores. Aquí se resta solo 1/3, así que elegir una opción al azar suma de media un noveno de acierto. Si eliminas una alternativa, la esperanza sube. El blanco conviene cuando ibas a marcar una opción que sabes falsa, no cuando no tienes ni idea.</p>
      <h3>Segundo ejercicio</h3>
      <p>Dos partes de dos horas, las dos con un mínimo de 5. La nota del ejercicio es la media. En el tema de composición pesan los conocimientos un 70 %, el análisis un 15 %, la expresión un 10 % y la presentación un 5 %. En el supuesto, análisis y conocimientos valen lo mismo. Después hay hasta quince minutos de diálogo.</p>
      <h3>Qué hacer con un suspenso en un tema</h3>
      <p>No repitas el simulacro entero al día siguiente. Abre el mapa de progreso, entrena veinte preguntas de los temas rojos y vuelve al simulacro cuando esos temas pasen de crema a verde.</p>
    </article>`;
}

function bind() {
  main.querySelectorAll("[data-action]").forEach((node) => {
    node.addEventListener("click", () => handleAction(node.dataset.action, node));
  });
  main.querySelectorAll("[data-topic]").forEach((node) => {
    node.addEventListener("click", () => {
      const id = Number(node.dataset.topic);
      const topics = new Set(state.setup.topics);
      if (topics.has(id)) topics.delete(id);
      else topics.add(id);
      state.setup.topics = [...topics];
      render();
    });
  });
  main.querySelectorAll("[data-choice]").forEach((node) => {
    node.addEventListener("click", () => choose(Number(node.dataset.choice)));
  });
  main.querySelectorAll("[data-jump]").forEach((node) => {
    node.addEventListener("click", () => {
      state.exam.index = Number(node.dataset.jump);
      saveExam();
      render();
    });
  });
  main.querySelectorAll("[data-filter]").forEach((node) => {
    node.addEventListener("click", () => {
      state.practicalFilter = node.dataset.filter;
      render();
    });
  });
  main.querySelectorAll("[data-focus-topic]").forEach((node) => {
    node.addEventListener("click", () => {
      state.setup.topics = [Number(node.dataset.focusTopic)];
    });
  });
  const count = main.querySelector("#count");
  if (count) {
    count.addEventListener("change", () => {
      state.setup.count = Number(count.value);
    });
  }
  const timer = main.querySelector("#with-timer");
  if (timer) timer.addEventListener("change", () => { state.setup.timer = timer.checked; });
  const study = main.querySelector("#study-mode");
  if (study) study.addEventListener("change", () => { state.setup.study = study.checked; });
}

function handleAction(action, node) {
  if (action === "simulacro") startExam({ mode: "simulacro" });
  if (action === "train") startExam({ mode: "entrenamiento", count: state.setup.count, timer: state.setup.timer, study: state.setup.study, topics: state.setup.topics });
  if (action === "fails") startExam({ mode: "repaso", ids: failedIds(), study: true });
  if (action === "group") {
    const group = node.dataset.group;
    const ids = BANK.syllabus.filter((topic) => topic.group === group).map((topic) => topic.id);
    const current = new Set(state.setup.topics);
    const allOn = ids.every((id) => current.has(id));
    ids.forEach((id) => (allOn ? current.delete(id) : current.add(id)));
    state.setup.topics = [...current];
    render();
  }
  if (action === "clear-topics") {
    state.setup.topics = [];
    render();
  }
  if (action === "prev") move(-1);
  if (action === "next") move(1);
  if (action === "blank") choose(null);
  if (action === "finish") submitExam();
  if (action === "reveal") {
    state.revealed[node.dataset.id] = !state.revealed[node.dataset.id];
    render();
  }
  if (action === "retry-weak") {
    const weak = Object.entries(state.exam.grade.byTopic)
      .filter(([, row]) => row.total && row.correct / row.total < 0.6)
      .map(([id]) => Number(id));
    startExam({ mode: "refuerzo", count: 20, study: true, topics: weak });
  }
}

function prepareQuestion(question, reserve) {
  const paired = question.choices.map((text, index) => ({ text, correct: index === question.answer }));
  const mixed = shuffle(paired);
  return {
    ...question,
    reserve,
    choices: mixed.map((item) => item.text),
    answer: mixed.findIndex((item) => item.correct),
  };
}

function pickStratified(pool, amount) {
  const byTopic = new Map();
  shuffle(pool).forEach((question) => {
    if (!byTopic.has(question.topic)) byTopic.set(question.topic, []);
    byTopic.get(question.topic).push(question);
  });
  const topics = shuffle([...byTopic.keys()].filter((topic) => topic !== 0));
  if (byTopic.has(0)) topics.push(0);
  const picked = [];
  const used = new Set();
  let guard = 0;
  while (picked.length < amount && guard < 5000) {
    guard += 1;
    let added = false;
    for (const topic of topics) {
      const list = byTopic.get(topic) || [];
      while (list.length && used.has(list[list.length - 1].id)) list.pop();
      const question = list.pop();
      if (!question || used.has(question.id)) continue;
      used.add(question.id);
      picked.push(question);
      added = true;
      if (picked.length >= amount) break;
    }
    if (!added) break;
  }
  return picked;
}

function startExam(options) {
  let pool = BANK.questions;
  if (options.ids) {
    const wanted = new Set(options.ids);
    pool = pool.filter((question) => wanted.has(question.id));
  } else if (options.topics && options.topics.length) {
    const wanted = new Set(options.topics);
    pool = pool.filter((question) => wanted.has(question.topic));
  }
  const preferred = pool.filter((question) => question.category !== "auxiliar");
  const auxiliar = pool.filter((question) => question.category === "auxiliar");
  let count = options.count || 20;
  let reserve = 0;
  let minutes = null;
  let title = "Entrenamiento";
  if (options.mode === "simulacro") {
    count = BANK.meta.questions;
    reserve = BANK.meta.reserve;
    minutes = BANK.meta.minutes;
    title = "Simulacro oficial";
  } else if (options.mode === "repaso") {
    count = Math.min(20, pool.length);
    title = "Repaso de fallos";
    minutes = options.timer ? count : null;
  } else if (options.timer) {
    minutes = count;
    title = "Entrenamiento cronometrado";
  }
  const target = Math.min(count + reserve, preferred.length + auxiliar.length);
  let picked = pickStratified(preferred, target);
  if (picked.length < target) {
    const more = pickStratified(auxiliar.filter((question) => !picked.some((item) => item.id === question.id)), target - picked.length);
    picked = picked.concat(more);
  }
  if (!picked.length) {
    window.alert("No hay preguntas para esa selección.");
    return;
  }
  const mainCount = Math.min(count, picked.length);
  const questions = [
    ...shuffle(picked.slice(0, mainCount)).map((question) => prepareQuestion(question, false)),
    ...shuffle(picked.slice(mainCount)).map((question) => prepareQuestion(question, true)),
  ];
  state.exam = {
    title,
    mode: options.mode,
    study: Boolean(options.study) && options.mode !== "simulacro",
    index: 0,
    questions,
    answers: {},
    submitted: false,
    started: Date.now(),
    endsAt: minutes ? Date.now() + minutes * 60 * 1000 : null,
    grade: null,
  };
  saveExam();
  go("/examen");
}

function choose(choice) {
  const exam = state.exam;
  if (!exam || exam.submitted) return;
  const question = exam.questions[exam.index];
  if (exam.study && exam.answers[question.id] !== undefined && exam.answers[question.id] !== null && choice !== null) return;
  exam.answers[question.id] = choice;
  saveExam();
  render();
}

function move(delta) {
  const exam = state.exam;
  if (!exam) return;
  exam.index = Math.min(exam.questions.length - 1, Math.max(0, exam.index + delta));
  saveExam();
  render();
}

function gradeExam(exam) {
  const main = exam.questions.filter((question) => !question.reserve);
  const byTopic = {};
  let correct = 0;
  let wrong = 0;
  let blank = 0;
  main.forEach((question) => {
    const answer = exam.answers[question.id];
    const row = byTopic[question.topic] || { correct: 0, wrong: 0, blank: 0, total: 0 };
    row.total += 1;
    if (answer === null || answer === undefined) {
      blank += 1;
      row.blank += 1;
    } else if (answer === question.answer) {
      correct += 1;
      row.correct += 1;
    } else {
      wrong += 1;
      row.wrong += 1;
    }
    byTopic[question.topic] = row;
  });
  const n = main.length || 1;
  const net = correct - wrong / 3;
  const score = Math.max(0, Math.round((net / n) * 1000) / 100);
  return {
    correct,
    wrong,
    blank,
    n: main.length,
    net,
    score,
    byTopic,
    pctCorrect: main.length ? (correct / main.length) * 100 : 0,
    pctWrong: main.length ? (wrong / main.length) * 100 : 0,
    pctBlank: main.length ? (blank / main.length) * 100 : 0,
  };
}

function submitExam(force) {
  const exam = state.exam;
  if (!exam || exam.submitted) return;
  const pending = exam.questions.filter((question) => !question.reserve && exam.answers[question.id] === undefined).length;
  if (!force && pending && !window.confirm(`Quedan ${pending} preguntas puntuables sin contestar. Se contarán en blanco. ¿Entregas?`)) return;
  exam.submitted = true;
  exam.grade = gradeExam(exam);
  exam.questions.filter((question) => !question.reserve).forEach((question) => {
    const record = state.stats.questions[question.id] || { ok: 0, bad: 0, blank: 0 };
    const answer = exam.answers[question.id];
    if (answer === null || answer === undefined) record.blank += 1;
    else if (answer === question.answer) record.ok += 1;
    else record.bad += 1;
    state.stats.questions[question.id] = record;
  });
  state.stats.exams.unshift({
    date: Date.now(),
    mode: exam.title,
    score: exam.grade.score,
    correct: exam.grade.correct,
    wrong: exam.grade.wrong,
    blank: exam.grade.blank,
  });
  state.stats.exams = state.stats.exams.slice(0, 30);
  saveStats();
  saveExam();
  go("/resultado");
}

function startTimer() {
  const node = document.querySelector("#timer");
  if (!node || !state.exam?.endsAt) return;
  state.timerId = setInterval(() => {
    const left = state.exam.endsAt - Date.now();
    if (left <= 0) {
      clearInterval(state.timerId);
      submitExam(true);
      return;
    }
    node.textContent = formatClock(left);
    node.classList.toggle("warning", left < 10 * 60 * 1000);
  }, 1000);
}

function formatClock(ms) {
  const total = Math.ceil(ms / 1000);
  const minutes = Math.floor(total / 60);
  const seconds = total % 60;
  return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}

function formatDate(stamp) {
  return new Intl.DateTimeFormat("es-ES", { dateStyle: "medium", timeStyle: "short" }).format(stamp);
}

function onKey(event) {
  if (state.route !== "/examen" || !state.exam || state.exam.submitted) return;
  if (event.metaKey || event.ctrlKey || event.altKey) return;
  if (event.key === "1" || event.key === "2" || event.key === "3") choose(Number(event.key) - 1);
  if (event.key === "ArrowRight") move(1);
  if (event.key === "ArrowLeft") move(-1);
  if (event.key === "Backspace") choose(null);
}

render();
