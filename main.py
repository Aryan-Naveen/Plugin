from plugin.word_filter import word_filter
from internal.background_filter import background_filter

words = ['frail','hesitant','spoil','sparkle','claim','table','quickest','measure','surprise','natural','rescue','fast']

filter = background_filter(plugins=[word_filter()])
filter.run(words)
