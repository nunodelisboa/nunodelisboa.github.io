---
layout: default
title: "Software archive"
permalink: /software/
description: "Software from the research years — motif discovery, miRNA prediction, logical modelling — kept as a legacy archive."
redirect_from:
  - /software.html
---

<div class="page-main">

  <div class="section-header">
    <span class="section-num">//</span>
    <h2>Software archive</h2>
  </div>

  <p class="section-intro">
    Everything here is legacy software from my research years — tools built for
    motif discovery, miRNA prediction and the logical modelling of gene
    regulatory networks. None of it is maintained any longer; what remains is
    kept as it was, for the record.
  </p>

  <div class="software-grid">
    {% assign projects = site.data.software.software %}
    {% for p in projects %}
    <article class="software-card">
      <span class="card-tag">Legacy — unmaintained</span>
      <h3>{{ p.name }}</h3>
      <p class="software-desc">{{ p.description }}</p>
      {% if p.note %}<p class="software-note">{{ p.note }}</p>{% endif %}
      {% if p.downloads %}
      <ul class="downloads">
        {% for d in p.downloads %}
        <li><a href="{{ '/' | append: d.path | relative_url }}">{{ d.label }}</a></li>
        {% endfor %}
      </ul>
      {% endif %}
      {% if p.url_or_path contains "://" %}
      <div class="software-links">
        <a href="{{ p.url_or_path }}" target="_blank" rel="noopener">Project site (archived) →</a>
      </div>
      {% endif %}
    </article>
    {% endfor %}
  </div>

</div>
