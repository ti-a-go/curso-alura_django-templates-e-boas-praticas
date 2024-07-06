https://docs.djangoproject.com/pt-br/5.0/ref/templates/language/


Filosofia

Django template system is not simply Python embedded into HTML. 

This is by design: the template system is meant to express presentation, not program logic.

The Django template system provides tags which function similarly to some programming constructs – an if tag for boolean tests, a for tag for looping, etc. – but these are not simply executed as the corresponding Python code, and the template system will not execute arbitrary Python expressions. 

Only the tags, filters and syntax listed below are supported by default (although you can add your own extensions to the template language as needed).

Templates

A template is a text file. It can generate any text-based format (HTML, XML, CSV, etc.).

A template contains variables, which get replaced with values when the template is evaluated, and tags, which control the logic of the template.

Below is a minimal template that illustrates a few basics. Each element will be explained later in this document.

```html
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
```

Filosofia

Why use a text-based template instead of an XML-based one (like Zope’s TAL)? We wanted Django’s template language to be usable for more than just XML/HTML templates. You can use the template language for any text-based format such as emails, JavaScript and CSV.

Variables

Variables look like this: `{{ variable }}`. When the template engine encounters a variable, it evaluates that variable and replaces it with the result. 

Variable names consist of any combination of alphanumeric characters and the underscore ("_") but may not start with an underscore, and may not be a number. 

The dot (".") also appears in variable sections, although that has a special meaning, as indicated below. 

Importantly, you cannot have spaces or punctuation characters in variable names.

Use a dot (.) to access attributes of a variable.

Por trás das cenas.

Technically, when the template system encounters a dot, it tries the following lookups, in this order:

1. Pesquisa pelo dicionário
2. Pesquisa pelo atributo ou método
3. Pesquisa pelo índice numérico

If the resulting value is callable, it is called with no arguments. The result of the call becomes the template value.

This lookup order can cause some unexpected behavior with objects that override dictionary lookup. For example, consider the following code snippet that attempts to loop over a collections.defaultdict:

```html
{% for k, v in defaultdict.items %}
    Do something with k and v here...
{% endfor %}
```

Because dictionary lookup happens first, that behavior kicks in and provides a default value instead of using the intended .items() method. In this case, consider converting to a dictionary first.


In the above example, `{{ section.title }}` will be replaced with the title attribute of the section object.

If you use a variable that doesn’t exist, the template system will insert the value of the string_if_invalid option, which is set to '' (the empty string) by default.

Note that “bar” in a template expression like {{ foo.bar }} will be interpreted as a literal string and not using the value of the variable “bar”, if one exists in the template context.

Variable attributes that begin with an underscore may not be accessed as they’re generally considered private.