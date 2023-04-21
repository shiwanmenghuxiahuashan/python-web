## 前言

解决如下问题：

1、MySQL 8. X 系列的安装流程

2、将MySQL安装到指定目录下

3、解决 mysql 8登录密码用caching_sha2_password验证的问题，常见的链接数据库错误如下：

PDO::__construct(): Unexpected server respose while doing caching_sha2 auth: 109

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b079016e935c4a03bf0ad50b4a8bad17~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1a6cee568e447ff9e9b65e37c5d0a92~tplv-k3u1fbpfcp-zoom-1.image)

下载地址：<https://dev.mysql.com/downloads/windows/installer/8.0.html>

## 1. 选择下载的版本

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26ee8fbb94514665b827dc13b058053e~tplv-k3u1fbpfcp-zoom-1.image)

  

## 2. 不听废话直接下载

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ecfd08c33484b51b5b77dd4f6b8ffbd~tplv-k3u1fbpfcp-zoom-1.image)

  

## 3. 开始安装

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6759aa910f9c40e08c9401054dbe507b~tplv-k3u1fbpfcp-zoom-1.image)

  

全家桶不推荐安装，大部分MySQL使用者都是本地开发学习使用，有个MySQL能练习语句就行，选择自定义安装即可。然后点 next。

如果要安装全家桶的话参考这个教程：<https://blog.csdn.net/xiezhiming1234/article/details/82860339>

## 4. 选择对应版本

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17eca4b7e007474db00d840b94e40c29~tplv-k3u1fbpfcp-zoom-1.image)

  

选中你要安装的MySQL版本，然后点绿色小箭头

## 5. 指定安装位置

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a76af8fff51435da14c9379d37ad060~tplv-k3u1fbpfcp-zoom-1.image)

  

点选右侧你要安装的MySQL，在下方显示Advance options(高级选项），点击高级选项指定安装位置。

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ac6dd299d3f4139a5826c72ff30b3c3~tplv-k3u1fbpfcp-zoom-1.image)

  

MySQL服务和数据目录都放在同一个地址下了，然后OK，OK, Next就行了

## 6. Next

此阶段，遇到Next点Next, 遇到Execute点Execute即可

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0792e7a298ce45b295a5a0be20051928~tplv-k3u1fbpfcp-zoom-1.image)

  

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23d7997409854b3b8daaa07d80333894~tplv-k3u1fbpfcp-zoom-1.image)

  

执行安装下载，需要等一会儿。

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a84337befd8c44bca4aa896593e51353~tplv-k3u1fbpfcp-zoom-1.image)

  

状态为完毕，然后Next

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa3c680810a14b0e99a0965ed96be90e~tplv-k3u1fbpfcp-zoom-1.image)

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a331cf878f84573831b1f5f87015ebe~tplv-k3u1fbpfcp-zoom-1.image)

  

继续下一步

## 7. 有坑，小心

mysql 8登录密码用caching_sha2_password验证，mysql 5用mysql_native_password，在安装的时候可以选择兼容老的安装模式，不然PHP链接数据库出错。

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5562936ed454dff8bd8db89a4b52db8~tplv-k3u1fbpfcp-zoom-1.image)

  

1处说的是使用强密码加密进行身份验证（推荐的），采用caching_sha2_password验证，但是这个不兼容MySQL5的密码验证方式。

2处说的是使用兼容方式验证，别废话，选 2！！！！

## 8. 设置密码

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4e62fe00e6d454495d18fae2a6c705a~tplv-k3u1fbpfcp-zoom-1.image)

  

## 9. 设置Window Service名称

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4beba0fa805c45228e809afba122742e~tplv-k3u1fbpfcp-zoom-1.image)

​

  

安装程序默认名称是“MySQL 80”，我因为业务需要，改成了MySQL，看个人意愿，该名称会注册到window的服务当中

## 10. Next

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996be6c7b22640fc9cf7ecfef5d866e3~tplv-k3u1fbpfcp-zoom-1.image)

​

  

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/930fb89eaf6b4226bcee8323b83bafbd~tplv-k3u1fbpfcp-zoom-1.image)

  

## 11. 完成安装

  

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365163c98b0d45489fe2f2b3750dea6d~tplv-k3u1fbpfcp-zoom-1.image)

​

  

## 参考资料

## 《windows系统 MySQL8.0.12详细安装步骤及基本使用教程》

全家桶的安装教程，地址：<https://blog.csdn.net/xiezhiming1234/article/details/82860339>

## 《一步一步详细介绍MySql8.0的安装流程》

MySQL命令行安装方法，地址：<https://www.cnblogs.com/wfhking/p/9510059.html>

## 《MySQL安装及MySQL8.0新密码认证方式 》

比较详细，说明了密码验证为啥选兼容的原因，地址：<https://blog.csdn.net/qq_26819733/article/details/80794047>
