# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r",encoding="UTF-8") as f:
    long_description = f.read()


packages = \
['nonebot_plugin_acc_calculate']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.4,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-acc-calculate',
    'version': '0.3.0',
    'description': 'Nonebot2 段位单曲acc计算',
    'long_description':long_description,
    'author': 'ohdmire',
    'author_email': '1750011571@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ohdmire/nonebot-plugin-acc-calculate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
