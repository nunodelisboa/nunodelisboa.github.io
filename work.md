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
    Twenty roles, 1999 to today — set on a true time scale: each role
    draws a line in its logo's colour for exactly as long as it lasted,
    and a year of line is a year of time. Fuller descriptions are on
    <a href="https://www.linkedin.com/in/nunodiasmendes" target="_blank" rel="noopener">LinkedIn</a>.
  </p>

  {% assign month_names = "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec" | split: "," %}
  {% assign axis_months = 348 %}
  {% assign stack_months_d = 3 %}
  {% assign stack_months_m = 5 %}

  {% comment %}
    Pre-pass: find the lowest stacked block bottom at each breakpoint.
    P(y, m) = (2026 - y + 1) * 12 - (m - 1), in months down from Jan 2027.
    A block occupies 4 months on desktop and 8 months on mobile,
    including the minimum gap before the next block.
  {% endcomment %}
  {% assign prev_bottom_d = 0 %}
  {% assign prev_bottom_m = 0 %}
  {% assign lane_bottom_1 = -1 %}
  {% assign lane_bottom_2 = -1 %}
  {% assign lane_bottom_3 = -1 %}
  {% assign lanes_csv = "" %}
  {% assign lanes_used = 1 %}
  {% assign tops_csv = "" %}
  {% assign bots_csv = "" %}
  {% for role in site.data.experience.experience %}
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
    {% assign mpos = 2026 | minus: ey | plus: 1 | times: 12 | minus: em | plus: 1 %}
    {% assign mpos_start = 2026 | minus: sy | plus: 1 | times: 12 | minus: sm | plus: 1 %}
    {% if lane_bottom_1 <= mpos %}{% assign lane = 0 %}{% assign lane_bottom_1 = mpos_start %}{% elsif lane_bottom_2 <= mpos %}{% assign lane = 1 %}{% assign lane_bottom_2 = mpos_start %}{% else %}{% assign lane = 2 %}{% assign lane_bottom_3 = mpos_start %}{% endif %}
    {% assign lanes_csv = lanes_csv | append: lane | append: "," %}
    {% assign tops_csv = tops_csv | append: mpos | append: "," %}
    {% assign bots_csv = bots_csv | append: mpos_start | append: "," %}
    {% assign lane_no = lane | plus: 1 %}{% if lane_no > lanes_used %}{% assign lanes_used = lane_no %}{% endif %}
    {% assign eff_d = mpos %}
    {% if prev_bottom_d > eff_d %}{% assign eff_d = prev_bottom_d %}{% endif %}
    {% assign prev_bottom_d = eff_d | plus: stack_months_d %}
    {% assign eff_m = mpos %}
    {% if prev_bottom_m > eff_m %}{% assign eff_m = prev_bottom_m %}{% endif %}
    {% assign prev_bottom_m = eff_m | plus: stack_months_m %}
  {% endfor %}
  {% assign tops = tops_csv | split: "," %}
  {% assign bots = bots_csv | split: "," %}
  {% assign lane_arr = lanes_csv | split: "," %}
  {% assign trim_t_csv = "" %}
  {% assign trim_b_csv = "" %}
  {% for role in site.data.experience.experience %}
    {% assign i = forloop.index0 %}
    {% assign mylane = lane_arr[i] | plus: 0 %}
    {% assign tt = 0 %}
    {% assign tb = 0 %}
    {% assign prev_j = -1 %}
    {% for lj in lane_arr %}{% assign lj_n = lj | plus: 0 %}{% if forloop.index0 < i and lj_n == mylane %}{% assign prev_j = forloop.index0 %}{% endif %}{% endfor %}
    {% if prev_j >= 0 %}{% assign pb = bots[prev_j] | plus: 0 %}{% assign mt = tops[i] | plus: 0 %}{% if pb == mt %}{% assign tt = 0.5 %}{% endif %}{% endif %}
    {% assign mybot = bots[i] | plus: 0 %}
    {% for lj in lane_arr %}{% assign lj_n = lj | plus: 0 %}{% if forloop.index0 > i and lj_n == mylane %}{% assign nt = tops[forloop.index0] | plus: 0 %}{% if mybot == nt %}{% assign tb = 0.5 %}{% endif %}{% break %}{% endif %}{% endfor %}
    {% assign trim_t_csv = trim_t_csv | append: tt | append: "," %}
    {% assign trim_b_csv = trim_b_csv | append: tb | append: "," %}
  {% endfor %}
  {% assign timeline_months_d = axis_months %}
  {% if prev_bottom_d > timeline_months_d %}{% assign timeline_months_d = prev_bottom_d %}{% endif %}
  {% assign timeline_months_m = axis_months %}
  {% if prev_bottom_m > timeline_months_m %}{% assign timeline_months_m = prev_bottom_m %}{% endif %}
  {% assign timeline_height_d = timeline_months_d | times: 44 | plus: 24 %}
  {% assign timeline_height_m = timeline_months_m | times: 48 | plus: 24 %}

  {% assign lanes = lanes_csv | split: "," %}
  {% assign trim_ts = trim_t_csv | split: "," %}
  {% assign trim_bs = trim_b_csv | split: "," %}
  <div class="timeline" style="--h-d: {{ timeline_height_d }}px; --h-m: {{ timeline_height_m }}px; --lanes: {{ lanes_used }}">
    {% for year in (1999..2026) %}
      {% assign tick_mpos = 2026 | minus: year | plus: 1 | times: 12 %}
      <span class="tl-tick" style="--mpos: {{ tick_mpos }}" aria-hidden="true"></span>
      <span class="tl-tick-label" style="--mpos: {{ tick_mpos }}" aria-hidden="true">{{ year }}</span>
    {% endfor %}

    {% assign prev_bottom_d = 0 %}
    {% assign prev_bottom_m = 0 %}
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
    {% assign mpos = 2026 | minus: ey | plus: 1 | times: 12 | minus: em | plus: 1 %}
    {% assign eff_d = mpos %}
    {% if prev_bottom_d > eff_d %}{% assign eff_d = prev_bottom_d %}{% endif %}
    {% assign push_d = eff_d | minus: mpos %}
    {% assign eff_m = mpos %}
    {% if prev_bottom_m > eff_m %}{% assign eff_m = prev_bottom_m %}{% endif %}
    {% assign push_m = eff_m | minus: mpos %}
    {% assign lane = lanes[forloop.index0] | plus: 0 %}
    {% assign tt = trim_ts[forloop.index0] %}{% assign tb = trim_bs[forloop.index0] %}
    <span class="tl-span" style="--mpos: {{ mpos }}; --span: {{ total_months }}; --lane: {{ lane }}; --c: {{ logo.color }}; --trim-top: {{ tt }}; --trim-bot: {{ tb }}; --push-d: {{ push_d }}; --push-m: {{ push_m }}" aria-hidden="true"></span>
    <div class="timeline-item tl-block{% unless role.end == 'present' %} past{% endunless %}" style="--mpos: {{ mpos }}; --push-d: {{ push_d }}; --push-m: {{ push_m }}; --lane: {{ lane }}; --c: {{ logo.color }}">
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
    {% assign prev_bottom_d = eff_d | plus: stack_months_d %}
    {% assign prev_bottom_m = eff_m | plus: stack_months_m %}
    {% endfor %}
  </div>

</div>
