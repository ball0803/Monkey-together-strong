from collections import Counter

# split given input
inputs = Counter(input().split())

m_key, m_value = inputs.most_common()[0]
l_key, l_value = inputs.most_common()[-1]
print(f'{m_key}{l_key} => {m_value + l_value}')
