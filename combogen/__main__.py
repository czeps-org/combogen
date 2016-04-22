from combogen.ChartGenerator import ChartGenerator, PROJECT_ROOT, TEMPLATE_ROOT, TRANSLATIONS_ROOT
from combogen.BackGenerator import BackGenerator
import os

chart_generator = ChartGenerator()
chart_generator.debug()
back_generator = BackGenerator()
back_generator.debug()

for file in os.listdir(TRANSLATIONS_ROOT):
  if (file.endswith(".json")):
    lang = file.split(".")[0]
    chart = chart_generator.generate(lang)
    back = back_generator.generate(lang)

    with open(os.path.join(PROJECT_ROOT, 'drug-combinations-{}.html'.format(lang)), 'w+') as f:
      f.write(chart)

    with open(os.path.join(PROJECT_ROOT, 'drug-combinations-back-{}.html'.format(lang)), 'w+') as f:
      f.write(back)
