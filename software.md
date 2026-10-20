---
layout: default
title: "Software archive"
permalink: /software/
description: "Software from the research years — motif discovery, miRNA prediction, logical modelling — kept as a legacy archive, plus one current GitHub project."
redirect_from:
  - /software.html
---

<div class="page-main">

  <div class="section-header">
    <span class="section-num">//</span>
    <h2>Software archive</h2>
  </div>

  <p class="section-intro">
    Almost everything here is legacy software from my research years — tools
    built for motif discovery, miRNA prediction and the logical modelling of
    gene regulatory networks. None of it is maintained any longer; the binaries
    and documentation are kept as they were, for the record. The one exception
    is the current project listed first.
  </p>

  <div class="software-grid">
    {% assign projects = site.data.software.software %}
    {% for p in projects %}{% if p.name == "modern-react-forms" %}
    <article class="software-card">
      <span class="card-tag current">Current project</span>
      <h3>{{ p.name }}</h3>
      <p class="software-desc">{{ p.description }}</p>
      {% if p.note %}<p class="software-note">{{ p.note }}</p>{% endif %}
      <div class="software-links">
        <a href="{{ p.url_or_path }}" target="_blank" rel="noopener">GitHub repository →</a>
      </div>
    </article>
    {% endif %}{% endfor %}
    {% for p in projects %}{% unless p.name == "modern-react-forms" %}
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
    {% endunless %}{% endfor %}
  </div>

</div>
