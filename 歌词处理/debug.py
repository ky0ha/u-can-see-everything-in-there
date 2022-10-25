a = '[00:17.670]来吧 现在开始吧'
import re
print(re.search(r'\d{2}:\d{2}.\d*$', a))