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

  {% assign scale_start = 1999 %}
  {% assign now_year = site.time | date: '%Y' | plus: 0 %}
  {% assign scale_end = 2026 %}
  {% if now_year > scale_end %}{% assign scale_end = now_year %}{% endif %}
  {% assign scale_span = scale_end | minus: scale_start %}
  {% assign decades = "2000,2010,2020" | split: "," %}
  {% assign month_names = "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec" | split: "," %}

  <div class="timeline">
    <div class="timeline-scale" aria-hidden="true">
      {% for d in decades %}
      {% assign dy = d | plus: 0 %}
      {% assign dpct = dy | minus: scale_start | times: 100.0 | divided_by: scale_span | round: 2 %}
      <span class="ts-tick" style="left: {{ dpct }}%"></span>
      <span class="ts-decade" style="left: {{ dpct }}%">{{ dy }}</span>
      {% endfor %}
      {% for role in site.data.experience.experience %}
      {% assign sy = role.start | split: ' ' | last | plus: 0 %}
      {% assign pct = sy | minus: scale_start | times: 100.0 | divided_by: scale_span | round: 2 %}
      <span class="ts-dot" style="left: {{ pct }}%" title="{{ role.org }} — {{ role.start }}"></span>
      {% endfor %}
      <span class="ts-label ts-label-start">{{ scale_start }}</span>
      <span class="ts-label ts-label-end">{{ scale_end }}</span>
    </div>

    {% assign prev_sy = 0 %}
    {% for role in site.data.experience.experience %}
    {% assign logo = site.data.logos[role.org] %}
    {% assign sy = role.start | split: ' ' | last | plus: 0 %}
    {% assign smon = role.start | split: ' ' | first %}
    {% assign sm = 1 %}{% for m in month_names %}{% if m == smon %}{% assign sm = forloop.index %}{% endif %}{% endfor %}
    {% if role.end == 'present' %}
    {% assign ey = site.time | date: '%Y' | plus: 0 %}
    {% assign em = site.time | date: '%m' | plus: 0 %}
    {% else %}
    {% assign ey = role.end | split: ' ' | last | plus: 0 %}
    {% assign emon = role.end | split: ' ' | first %}
    {% assign em = 1 %}{% for m in month_names %}{% if m == emon %}{% assign em = forloop.index %}{% endif %}{% endfor %}
    {% endif %}
    {% assign total_months = ey | minus: sy | times: 12 | plus: em | minus: sm | plus: 1 %}
    {% assign dur_mos = total_months | modulo: 12 %}
    {% assign dur_yrs = total_months | minus: dur_mos | divided_by: 12 %}
    {% capture duration %}{% if dur_yrs > 0 %}{{ dur_yrs }} yr{% if dur_yrs > 1 %}s{% endif %}{% endif %}{% if dur_yrs > 0 and dur_mos > 0 %}{{ ' ' }}{% endif %}{% if dur_mos > 0 %}{{ dur_mos }} mo{% if dur_mos > 1 %}s{% endif %}{% endif %}{% endcapture %}
    {% assign gap_px = 0 %}
    {% if forloop.index > 1 %}
    {% assign gap_px = prev_sy | minus: sy | times: 12 %}
    {% if gap_px > 72 %}{% assign gap_px = 72 %}{% endif %}
    {% if gap_px < 0 %}{% assign gap_px = 0 %}{% endif %}
    {% endif %}
    <div class="timeline-item{% unless role.end == 'present' %} past{% endunless %}"{% if forloop.index > 1 %} style="--gap: {{ gap_px }}px"{% endif %}>
      {% if logo %}
      <div class="org-logo{% if logo.dark %} org-logo-dark{% endif %}"><img src="{{ '/assets/img/logos/' | append: logo.file | relative_url }}" alt="{{ role.org }} logo" loading="lazy"></div>
      {% endif %}
      <div class="timeline-body">
        <div class="timeline-meta">{{ role.start }} – {% if role.end == 'present' %}Present{% else %}{{ role.end }}{% endif %} · {{ role.location }}{% if role.end == 'present' %} · Current role{% endif %}{% if duration != '' %} · {{ duration }}{% endif %}</div>
        <div class="timeline-title">{{ role.title }}</div>
        <div class="timeline-company">{{ role.org }}</div>
        {% if role.concurrent %}
        <div class="timeline-tags"><span class="tag">Concurrent</span></div>
        {% endif %}
      </div>
    </div>
    {% assign prev_sy = sy %}
    {% endfor %}
  </div>

</div>
