<div align="center">

<img src="assets/banner.svg" alt="Peter Isberg. Software developer and author. Guardrails for the machines that write the code. Gothenburg, Sweden." width="100%" />

<p>
<a href="http://www.deversity.se"><img src="https://img.shields.io/badge/deversity.se-111B2E?style=for-the-badge&logo=googlechrome&logoColor=F97316" alt="Website: deversity.se" /></a>
<a href="mailto:isberg.peter@gmail.com"><img src="https://img.shields.io/badge/Email-111B2E?style=for-the-badge&logo=gmail&logoColor=F97316" alt="Email" /></a>
<a href="https://www.amazon.com/Vibe-Coding-Architecture-Scale-AI-assisted-ebook/dp/B0HF3MLBB8"><img src="https://img.shields.io/badge/The_book-111B2E?style=for-the-badge&logo=bookstack&logoColor=F97316" alt="Vibe Coding Architecture at Scale on Amazon" /></a>
<a href="https://github.com/PIsberg?tab=followers"><img src="https://img.shields.io/github/followers/PIsberg?style=for-the-badge&logo=github&logoColor=F97316&label=Followers&color=111B2E&labelColor=111B2E" alt="GitHub followers" /></a>
</p>

</div>

## About

I am a software developer in Gothenburg, Sweden, working mostly in Java. My open source work
keeps returning to one question: when AI agents write most of the code, what keeps the system
correct?

My answers so far are annotations that fence off the code an agent must not touch, tests that
force concurrency bugs to reproduce on demand, a local firewall against prompt injection, and
a book about the architecture that holds it all together.

Ask me about Java, AI guardrails, static analysis, MCP servers, and why a green test suite is
not proof.

## The book

<table>
<tr>
<td width="250" align="center">
<a href="https://www.amazon.com/Vibe-Coding-Architecture-Scale-AI-assisted-ebook/dp/B0HF3MLBB8"><img src="assets/book-cover.jpg" alt="Cover of Vibe Coding Architecture at Scale" width="220" /></a>
</td>
<td>

### Vibe Coding Architecture at Scale

**Vibe coding gives you speed. Vibe Architecture gives you scale.**

When syntax is free, structure is your only asset. This is the book on designing, scaling and
guardrailing large-scale systems in the age of AI orchestration.

<a href="https://www.amazon.com/Vibe-Coding-Architecture-Scale-AI-assisted-ebook/dp/B0HF3MLBB8"><img src="https://img.shields.io/badge/Get_it_on_Amazon-F97316?style=for-the-badge" alt="Get Vibe Coding Architecture at Scale on Amazon" /></a>

</td>
</tr>
</table>

## Open source

<table>
<tr><th align="left" width="170">Project</th><th align="left">What it does</th><th align="left" width="80">Stars</th></tr>
<tr><td colspan="3"><b>Guardrails for AI agents</b></td></tr>
<tr>
<td><a href="https://github.com/PIsberg/vibetags"><b>vibetags</b></a></td>
<td>Java annotations as AI guardrails. Mark the code an agent must not rewrite, and it stops rewriting it.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/vibetags?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="vibetags stars" /></td>
</tr>
<tr>
<td><a href="https://github.com/PIsberg/llm-fw"><b>llm-fw</b></a></td>
<td>Local prompt injection firewall. Malicious prompts are blocked and logged, clean ones pass through.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/llm-fw?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="llm-fw stars" /></td>
</tr>
<tr>
<td><a href="https://github.com/PIsberg/axiom"><b>axiom</b></a></td>
<td>The codebase as a live queryable graph, so an agent can see what it just broke.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/axiom?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="axiom stars" /></td>
</tr>
<tr>
<td><a href="https://github.com/PIsberg/skill3"><b>skill3</b></a></td>
<td>Relearns a technical skill for an agent, anchored to a target model cutoff, and vets the result.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/skill3?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="skill3 stars" /></td>
</tr>
<tr>
<td><a href="https://github.com/PIsberg/ghost-mcp"><b>ghost-mcp</b></a></td>
<td>MCP server that exposes OS level UI automation to AI clients.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/ghost-mcp?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="ghost-mcp stars" /></td>
</tr>
<tr><td colspan="3"><b>Java correctness and analysis</b></td></tr>
<tr>
<td><a href="https://github.com/PIsberg/async-test-lib"><b>async-test-lib</b></a></td>
<td>Forces concurrency bugs to happen using synchronized barriers, then names the one that fired.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/async-test-lib?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="async-test-lib stars" /></td>
</tr>
<tr>
<td><a href="https://github.com/PIsberg/codekoll"><b>codekoll</b></a></td>
<td>Static analyzer for Java that finds the bugs which compile perfectly and detonate in production.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/codekoll?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="codekoll stars" /></td>
</tr>
<tr>
<td><a href="https://github.com/PIsberg/codekarta"><b>codekarta</b></a></td>
<td>Parses Java source and emits SVG maps: call graphs, exception flow, state machines.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/codekarta?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="codekarta stars" /></td>
</tr>
<tr>
<td><a href="https://github.com/PIsberg/blindbean"><b>blindbean</b></a></td>
<td>Homomorphic encryption hidden behind ordinary Java objects and annotations.</td>
<td><img src="https://img.shields.io/github/stars/PIsberg/blindbean?style=flat-square&label=%20&logo=github&logoColor=F97316&color=111B2E&labelColor=111B2E" alt="blindbean stars" /></td>
</tr>
</table>

## Toolbox

<table>
<tr>
<td><b>Primary</b></td>
<td>
<img src="https://img.shields.io/badge/Java-111B2E?style=flat-square&logo=openjdk&logoColor=F97316" alt="Java" height="24" />
<img src="https://img.shields.io/badge/Spring_Boot-111B2E?style=flat-square&logo=springboot&logoColor=F97316" alt="Spring Boot" height="24" />
<img src="https://img.shields.io/badge/Gradle-111B2E?style=flat-square&logo=gradle&logoColor=F97316" alt="Gradle" height="24" />
<img src="https://img.shields.io/badge/Maven-111B2E?style=flat-square&logo=apachemaven&logoColor=F97316" alt="Maven" height="24" />
</td>
</tr>
<tr>
<td><b>Also fluent</b></td>
<td>
<img src="https://img.shields.io/badge/Rust-111B2E?style=flat-square&logo=rust&logoColor=F97316" alt="Rust" height="24" />
<img src="https://img.shields.io/badge/TypeScript-111B2E?style=flat-square&logo=typescript&logoColor=F97316" alt="TypeScript" height="24" />
<img src="https://img.shields.io/badge/Go-111B2E?style=flat-square&logo=go&logoColor=F97316" alt="Go" height="24" />
<img src="https://img.shields.io/badge/Python-111B2E?style=flat-square&logo=python&logoColor=F97316" alt="Python" height="24" />
</td>
</tr>
<tr>
<td><b>Platform and AI</b></td>
<td>
<img src="https://img.shields.io/badge/Docker-111B2E?style=flat-square&logo=docker&logoColor=F97316" alt="Docker" height="24" />
<img src="https://img.shields.io/badge/GitHub_Actions-111B2E?style=flat-square&logo=githubactions&logoColor=F97316" alt="GitHub Actions" height="24" />
<img src="https://img.shields.io/badge/Claude-111B2E?style=flat-square&logo=anthropic&logoColor=F97316" alt="Claude" height="24" />
<img src="https://img.shields.io/badge/MCP-111B2E?style=flat-square&logo=modelcontextprotocol&logoColor=F97316" alt="Model Context Protocol" height="24" />
<img src="https://img.shields.io/badge/Linux-111B2E?style=flat-square&logo=linux&logoColor=F97316" alt="Linux" height="24" />
<img src="https://img.shields.io/badge/IntelliJ_IDEA-111B2E?style=flat-square&logo=intellijidea&logoColor=F97316" alt="IntelliJ IDEA" height="24" />
</td>
</tr>
</table>

## Activity

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

---

<div align="center">
<sub>Get in touch: <a href="mailto:isberg.peter@gmail.com">isberg.peter@gmail.com</a> · <a href="http://www.deversity.se">deversity.se</a></sub>
</div>
