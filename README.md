<!--
  Every image under assets/cards and assets/ui is generated: edit the tables in
  tools/gen_assets.py and run `python tools/gen_assets.py`. Only assets/banner.svg is hand-drawn.
-->

<div align="center">

<img src="assets/banner.svg" alt="Peter Isberg. Software developer and author. Guardrails for the machines that write the code. Gothenburg, Sweden." width="100%" />

<p>
<a href="https://www.amazon.com/Vibe-Coding-Architecture-Scale-AI-assisted-ebook/dp/B0HF3MLBB8"><img src="assets/ui/btn-book.svg" alt="Read the book" width="190" /></a>
<a href="http://www.deversity.se"><img src="assets/ui/btn-site.svg" alt="deversity.se" width="190" /></a>
<a href="mailto:isberg.peter@gmail.com"><img src="assets/ui/btn-email.svg" alt="Email me" width="190" /></a>
</p>

</div>

<img src="assets/ui/section-01.svg" alt="About" width="100%" />

I am a software developer in Gothenburg, Sweden, working mostly in Java. My open source work
keeps returning to one question: when AI agents write most of the code, what keeps the system
correct?

My answers so far are annotations that fence off the code an agent must not touch, tests that
force concurrency bugs to reproduce on demand, a local firewall against prompt injection, and
a book about the architecture that holds it all together.

Ask me about Java, AI guardrails, static analysis, MCP servers, and why a green test suite is
not proof.

<img src="assets/ui/section-02.svg" alt="The book" width="100%" />

<p align="center">
<a href="https://www.amazon.com/Vibe-Coding-Architecture-Scale-AI-assisted-ebook/dp/B0HF3MLBB8"><img src="assets/book-cover.jpg" alt="Cover of Vibe Coding Architecture at Scale" width="24%" /></a>
<a href="https://www.amazon.com/Vibe-Coding-Architecture-Scale-AI-assisted-ebook/dp/B0HF3MLBB8"><img src="assets/ui/book-panel.svg" alt="Vibe Coding Architecture at Scale. Vibe coding gives you speed. Vibe Architecture gives you scale. When syntax is free, structure is your only asset. Get it on Amazon." width="74%" /></a>
</p>

<img src="assets/ui/section-03.svg" alt="How it fits together" width="100%" />

Eight of these projects are stations on one line: the path a change takes from an AI agent to
production.

<img src="assets/ui/pipeline.svg" alt="Pipeline from AI agent to production. Before it writes: skill3 teaches the agent current skills, llm-fw filters prompts before the model. While it writes: vibetags fences off code it must not touch, axiom shows what a change just broke, ghost-mcp gives it hands on the desktop. Before it ships: codekoll runs static analysis for silent bugs, async-test-lib forces concurrency bugs to fire, codekarta maps what was actually built." width="100%" />

<img src="assets/ui/section-04.svg" alt="Open source" width="100%" />

### Guardrails for AI agents

<p align="center">
<a href="https://github.com/PIsberg/vibetags"><img src="assets/cards/vibetags.svg" alt="vibetags: Java annotations as AI guardrails. Mark the code an agent must not rewrite, and it stops rewriting it. Works with Claude, Cursor and Codex." width="100%" /></a>
<a href="https://github.com/PIsberg/llm-fw"><img src="assets/cards/llm-fw.svg" alt="llm-fw: Local prompt injection firewall. Malicious prompts are blocked and logged, clean ones pass through." width="49.5%" /></a>
<a href="https://github.com/PIsberg/axiom"><img src="assets/cards/axiom.svg" alt="axiom: The codebase as a live queryable graph, so an agent can see what it just broke." width="49.5%" /></a>
<a href="https://github.com/PIsberg/skill3"><img src="assets/cards/skill3.svg" alt="skill3: Relearns a technical skill for an agent, anchored to a target model cutoff, and vets the result." width="49.5%" /></a>
<a href="https://github.com/PIsberg/ghost-mcp"><img src="assets/cards/ghost-mcp.svg" alt="ghost-mcp: MCP server that exposes OS level UI automation to AI clients." width="49.5%" /></a>
</p>

### Java correctness and analysis

<p align="center">
<a href="https://github.com/PIsberg/async-test-lib"><img src="assets/cards/async-test-lib.svg" alt="async-test-lib: Forces concurrency bugs to happen using synchronized barriers, then names the one that fired." width="49.5%" /></a>
<a href="https://github.com/PIsberg/codekoll"><img src="assets/cards/codekoll.svg" alt="codekoll: Static analyzer for Java that finds the bugs which compile perfectly and detonate in production." width="49.5%" /></a>
<a href="https://github.com/PIsberg/codekarta"><img src="assets/cards/codekarta.svg" alt="codekarta: Parses Java source and emits SVG maps: call graphs, exception flow, state machines." width="49.5%" /></a>
<a href="https://github.com/PIsberg/blindbean"><img src="assets/cards/blindbean.svg" alt="blindbean: Homomorphic encryption hidden behind ordinary Java objects and annotations." width="49.5%" /></a>
</p>

<img src="assets/ui/section-05.svg" alt="Toolbox" width="100%" />

<img src="assets/ui/toolbox.svg" alt="Primary: Java, Spring Boot, Gradle, Maven. Also fluent: Rust, TypeScript, Go, Python. Platform and AI: Docker, GitHub Actions, Claude, MCP, Linux, IntelliJ IDEA." width="100%" />

<img src="assets/ui/section-06.svg" alt="Activity" width="100%" />

<div align="center">

<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=PIsberg&theme=github_dark" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=PIsberg&theme=github" alt="GitHub contribution stats" height="190" />
</picture>
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=PIsberg&theme=github_dark" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=PIsberg&theme=github" alt="Repositories per language" height="190" />
</picture>

</div>

<br />

<a href="mailto:isberg.peter@gmail.com"><img src="assets/ui/footer.svg" alt="Building with AI agents and want it to stay correct? Get in touch: isberg.peter@gmail.com" width="100%" /></a>

<div align="center">
<sub><a href="mailto:isberg.peter@gmail.com">isberg.peter@gmail.com</a> · <a href="http://www.deversity.se">deversity.se</a></sub>
</div>
