from string import Template


# String template
# Unix Shell


tmpl = Template("Hello!!!,Mr.$who $what a talent")
print(tmpl.substitute(who="Sachin", what="Talent"))
