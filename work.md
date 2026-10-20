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
    The dated record: twenty roles, from a part-time customer-support job in
    1999 through a doctorate, two postdocs and a decade of industry, to Meta.
    Titles and dates follow my LinkedIn profile, which is also where the
    fuller descriptions live. Two entries — NOS and BOLD by Devoteam — are
    marked concurrent: BOLD was the contracting firm, NOS the client, over the
    same period.
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

  <p class="section-intro" style="margin-top: 1rem;">
    Fuller role descriptions are on
    <a href="https://www.linkedin.com/in/nunodiasmendes" target="_blank" rel="noopener">LinkedIn</a>.
    The academic years behind the middle of this timeline are archived under
    <a href="{{ '/research/' | relative_url }}">Research</a>,
    <a href="{{ '/software/' | relative_url }}">Software</a> and
    <a href="{{ '/teaching/' | relative_url }}">Teaching</a>.
  </p>

</div>
