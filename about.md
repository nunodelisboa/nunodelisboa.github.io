---
layout: default
title: "About"
permalink: /about/
description: "About Nuno D. Mendes — Senior Software Engineer at Meta in New York; dual PhD in Computational Biology (IST · Lyon 1, 2011); education, languages and recommendations."
redirect_from:
  - /shortcv.html
---

<div class="page-main">

  <div class="section-header">
    <span class="section-num">//</span>
    <h2>About</h2>
  </div>

  <p class="section-intro" style="margin-top: 0;">
    I'm a Senior Software Engineer at Meta in New York. I arrived in industry
    from research: a dual PhD in Computational Biology from Instituto
    Superior Técnico and Université Claude Bernard Lyon 1 (2011), postdoctoral
    years in Lisbon and Oeiras, then Lisbon's tech scene — Pentaho, and
    Practio, where I led the Lisbon team — and health-tech in New York with
    Heartbeat Health, before Meta in 2021.
  </p>
  <p class="section-intro">
    The through-line: algorithms for DNA, then platforms for health, now
    infrastructure at scale. I live in New York now; Lisbon is where I come from. The
    academic work — <a href="{{ '/research/' | relative_url }}">publications</a>,
    <a href="{{ '/software/' | relative_url }}">software</a> and
    <a href="{{ '/teaching/' | relative_url }}">teaching</a> — stays on this
    site as an archive of that earlier career.
  </p>

  <div class="pub-section">
    <h3 class="pub-section-title">Education</h3>
    <div class="edu-grid" style="margin-top: 1.5rem;">
      {% for edu in site.data.education.education %}
      <div class="edu-card">
        <div class="edu-degree">{{ edu.degree }}</div>
        <div class="edu-school">{{ edu.institution }}</div>
        <div class="edu-years">{% if edu.start == edu.end %}{{ edu.end }}{% else %}{{ edu.start }}–{{ edu.end }}{% endif %}</div>
      </div>
      {% endfor %}
    </div>
    <p class="software-note" style="margin-top: 1.2rem;">
      The two PhD entries are a single dual award — one thesis, two diplomas:
      “Efficient algorithms for the identification of miRNA motifs in DNA
      sequences”, supervised by Ana T. Freitas (IST) and Marie-France Sagot
      (Lyon), entered via the Gulbenkian PhD Programme in Computational
      Biology.
    </p>
  </div>

  <div class="pub-section">
    <h3 class="pub-section-title">Languages</h3>
    <div class="skill-list" style="margin-top: 1.2rem;">
      <span class="skill-pill">Portuguese — Native</span>
      <span class="skill-pill">English — Full professional</span>
      <span class="skill-pill">French — Full professional</span>
      <span class="skill-pill">Spanish — Professional working</span>
    </div>
  </div>

  <div class="pub-section">
    <h3 class="pub-section-title">Recommendations</h3>
    <p class="software-note">
      Received on LinkedIn over the years; the full texts live there.
    </p>
    <ul class="pub-list">
      <li class="pub-item">
        <div class="pub-title">Samuel Coelho</div>
        <div class="pub-meta">Recommendation received · 2022</div>
      </li>
      <li class="pub-item">
        <div class="pub-title">Allan Ebdrup</div>
        <div class="pub-meta">Recommendation received · 2020</div>
      </li>
      <li class="pub-item">
        <div class="pub-title">Ricardo Cerqueira</div>
        <div class="pub-meta">Recommendation received · 2004</div>
      </li>
    </ul>
  </div>

  <div class="hero-links" style="opacity: 1; animation: none;">
    <a href="https://www.linkedin.com/in/nunodiasmendes" target="_blank" rel="noopener" class="btn btn-primary">LinkedIn</a>
    <a href="https://github.com/nunodelisboa" target="_blank" rel="noopener" class="btn btn-ghost">GitHub</a>
  </div>

</div>
