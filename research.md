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
    {% if key == 'theses' %}
    <div class="skill-group-title" style="margin-top: 1.2rem;">Theses — read in the page</div>
    <div class="pdf-viewer" data-pdf-viewer>
      <div class="pdf-doc-list" role="group" aria-label="Theses">
        <button type="button" class="pdf-doc is-active" aria-pressed="true" data-pdf-title="PhD thesis — first 20 pages (preview)" data-pdf-src="{{ '/documents/phd-thesis-preview.pdf' | relative_url }}">PhD thesis — first 20 pages (preview)</button>
        <button type="button" class="pdf-doc" aria-pressed="false" data-pdf-title="Master's thesis (2005)" data-pdf-src="{{ '/pub/publications/05-MscThesis/05-ndm-msc-thesis.pdf' | relative_url }}">Master's thesis (2005)</button>
      </div>
      <iframe data-pdf-frame title="PhD thesis — first 20 pages (preview)" src="{{ '/documents/phd-thesis-preview.pdf' | relative_url }}"></iframe>
      <p class="pdf-fallback">PDF not rendering? <a data-pdf-open href="{{ '/documents/phd-thesis-preview.pdf' | relative_url }}" target="_blank" rel="noopener">Open PhD thesis — first 20 pages (preview) directly ↗</a> · Full PhD thesis: <a href="{{ '/pub/publications/11-PhDThesis/11-ndm-phd-thesis.pdf.gz' | relative_url }}">PDF (.gz)</a></p>
    </div>
    {% endif %}
    {% if key == 'technical_reports' %}
    <div class="skill-group-title" style="margin-top: 1.2rem;">Graduation thesis — read in the page</div>
    <div class="pdf-viewer" data-pdf-viewer>
      <div class="pdf-doc-list" role="group" aria-label="Graduation thesis">
        <button type="button" class="pdf-doc is-active" aria-pressed="true" data-pdf-title="Graduation thesis / TFC (2004)" data-pdf-src="{{ '/pub/publications/04-TFC/04-ndm-tfc.pdf' | relative_url }}">Graduation thesis / TFC (2004)</button>
      </div>
      <iframe data-pdf-frame title="Graduation thesis / TFC (2004)" src="{{ '/pub/publications/04-TFC/04-ndm-tfc.pdf' | relative_url }}"></iframe>
      <p class="pdf-fallback">PDF not rendering? <a data-pdf-open href="{{ '/pub/publications/04-TFC/04-ndm-tfc.pdf' | relative_url }}" target="_blank" rel="noopener">Open Graduation thesis / TFC (2004) directly ↗</a></p>
    </div>
    {% endif %}
  </div>
  {% endfor %}

</div>

<script>
(function () {
  var viewers = document.querySelectorAll('[data-pdf-viewer]');
  Array.prototype.forEach.call(viewers, function (viewer) {
    var frame = viewer.querySelector('[data-pdf-frame]');
    var openLink = viewer.querySelector('[data-pdf-open]');
    var docs = viewer.querySelectorAll('.pdf-doc');
    if (!frame) { return; }
    Array.prototype.forEach.call(docs, function (doc) {
      doc.addEventListener('click', function () {
        Array.prototype.forEach.call(docs, function (other) {
          other.classList.remove('is-active');
          other.setAttribute('aria-pressed', 'false');
        });
        doc.classList.add('is-active');
        doc.setAttribute('aria-pressed', 'true');
        var src = doc.getAttribute('data-pdf-src');
        var title = doc.getAttribute('data-pdf-title');
        frame.setAttribute('src', src);
        frame.setAttribute('title', title);
        if (openLink) {
          openLink.setAttribute('href', src);
          openLink.textContent = 'Open ' + title + ' directly ↗';
        }
      });
    });
  });
})();
</script>
