# パッケージインストールのための設定（かな？）
from setuptools import setup, find_packages

setup(
    name='myconmo',    #パッケージ名
    version="0.0.2",
    description="My config modules",
    author='Kemmotsu',
    license='MIT',
)

# setup.pyがあるフォルダから以下コマンドを実行することでパッケージインストール可能
# pip install -e .

# 使用するときは、 import myconmo を宣言。
# そしてmyconmo.<__init__.pyの__all__で定義した名称>でモジュールを利用できる