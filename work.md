---
layout: default
title: "Work"
permalink: /work/
description: "Career timeline of Nuno D. Mendes — twenty roles from a first job in customer support in 1999 to Senior Software Engineer at Meta."
---

<div class="page-main">

  <div class="section-header">
    <span class="section-num">//</span>
    <h2>Work</h2>
  </div>

  <p class="section-intro">
    Twenty roles, 1999 to today. Fuller descriptions are on
    <a href="https://www.linkedin.com/in/nunodiasmendes" target="_blank" rel="noopener">LinkedIn</a>.
  </p>

  <div class="timeline">
    {% for role in site.data.experience.experience %}
    <div class="timeline-item{% unless role.end == 'present' %} past{% endunless %}">
      <div class="timeline-meta">{{ role.start }} – {% if role.end == 'present' %}Present{% else %}{{ role.end }}{% endif %} · {{ role.location }}{% if role.end == 'present' %} · Current role{% endif %}</div>
      <div class="timeline-title">{{ role.title }}</div>
      <div class="timeline-company">{{ role.org }}</div>
      {% if role.concurrent %}
      <div class="timeline-tags"><span class="tag">Concurrent</span></div>
      {% endif %}
    </div>
    {% endfor %}
  </div>

</div>
