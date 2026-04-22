---
title: Team
nav_order: 8
permalink: /team/
---

# Team

{% assign team = site.staffers | sort: "name" %}
<div class="staff">
{% for staffer in team %}
  {{ staffer.content | default: staffer.excerpt }}
{% endfor %}
</div>
