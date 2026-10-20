---
layout: default
title: "Research archive"
permalink: /research/
description: "Complete publication record from an academic career in computational biology, 2004–2018 — journal papers, book chapter, conference paper, abstracts, theses and talks, kept for citation."
redirect_from:
  - /publications.html
  - /research.html
  - /documents.html
---

<div class="page-main">

  <div class="section-header">
    <span class="section-num">//</span>
    <h2>Research archive</h2>
  </div>

  <p class="section-intro">
    These are the publications of my academic career in computational biology,
    from 2004 to 2018 — doctoral and postdoctoral years in Lisbon and Lyon that
    ended when I moved into industry full-time. The list is kept complete, as a
    record for citation; it is not current work. These papers reflect the
    knowledge of their time; where a field has moved on, a brief note says so.
  </p>

  {% for section in site.data.publications %}
  {% assign key = section[0] %}
  {% assign items = section[1] %}
  <div class="pub-section">
    <h3 class="pub-section-title">{% case key %}{% when 'journal_papers' %}Journal papers{% when 'book_chapter' %}Book chapter{% when 'conference' %}Conference{% when 'abstracts_posters' %}Abstracts &amp; posters{% when 'theses' %}Theses{% when 'technical_reports' %}Technical reports{% when 'talks' %}Talks{% else %}{{ key }}{% endcase %}</h3>
    <ul class="pub-list">
      {% for item in items %}
      <li class="pub-item">
        <div class="pub-title">{{ item.title }}</div>
        {% if item.authors %}<div class="pub-authors">{{ item.authors }}</div>{% endif %}
        <div class="pub-meta">
          <span class="pub-venue">{{ item.venue }}</span> · {{ item.year }}
          {% if item.pdf %} · <a href="{{ '/' | append: item.pdf | relative_url }}">PDF</a>{% endif %}
          {% if item.url %} · <a href="{{ item.url }}" target="_blank" rel="noopener">Publisher</a>{% endif %}
        </div>
      </li>
      {% if item.title contains "Current tools for the identification of miRNA" %}
      <li class="pub-item context-note-item">
        <aside class="context-note">
          <div class="context-note-label">Then &amp; now — miRNA</div>
          <p>
            Context, from the vantage point of today: this work dates from a period
            when miRNA catalogues were expanding rapidly and target identification
            was largely computational prediction. Since then the field has been
            recognised at the highest level — the 2024 Nobel Prize in Physiology or
            Medicine went to Victor Ambros and Gary Ruvkun for the discovery of
            microRNA — and it has also corrected itself: large-scale reannotation
            (miRBase high-confidence sets, MirGeneDB) pruned many early catalogue
            entries as fragments or false positives; AGO CLIP-seq experiments
            shifted target identification from pure prediction toward measured
            binding; isomiRs and non-canonical biogenesis complicated the
            one-sequence–one-miRNA picture; and circulating miRNAs were explored as
            biomarkers, with mixed reproducibility. These papers are the state of
            the art of their moment, not a summary of current miRNA biology.
          </p>
        </aside>
      </li>
      {% endif %}
      {% endfor %}
    </ul>
  </div>
  {% endfor %}

</div>
