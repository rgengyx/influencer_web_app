import pandas as pd
import numpy as np

df1 = pd.DataFrame({'id': list(range(1,401)), 'product_order': list(range(1,11)) * 40, 'review_order': list(range(1,401))})

df1.to_csv('csv/latin_product_review.csv')




import pandas as pd
import numpy as np
import random

random.seed(42)

df2 = pd.DataFrame({'review_order': list(range(1,401)), \
    'p1': [random.randint(1,6) for i in range(1,401)], \
        'p2': [random.randint(1,6) for i in range(1,401)], \
            'p3': [random.randint(1,6) for i in range(1,401)], \
                'p4': [random.randint(1,6) for i in range(1,401)], \
                    'p5': [random.randint(1,6) for i in range(1,401)], \
                        'p6': [random.randint(1,6) for i in range(1,401)], \
                            'p7': [random.randint(1,6) for i in range(1,401)], \
                                'p8': [random.randint(1,6) for i in range(1,401)], \
                                    'p9': [random.randint(1,6) for i in range(1,401)], \
                                        'p10': [random.randint(1,6) for i in range(1,401)] \
        })

df2.to_csv('csv/latin_product_map.csv')