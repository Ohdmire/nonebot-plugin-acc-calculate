# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r",encoding="UTF-8") as f:
    long_description = f.read()

setuptools.setup(
    name="nonebot-plugin-acc-calculate",
    version="0.3.2",
    author="ohdmire",
    author_email="1750011571@qq.com",
    description="Nonebot2 段位单曲acc计算",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ohdmire/nonebot-plugin-acc-calculate",
    project_urls={
        "Bug Tracker": "https://github.com/ohdmire/nonebot-plugin-acc-calculate/issues",
    },
    packages=["nonebot_plugin_acc_calculate"],
    python_requires=">=3.8,<4.0",
    install_requires=[
        "nonebot2>=2.0.0a16",
        "nonebot-adapter-onebot>=2.0.0b1",
    ],
)