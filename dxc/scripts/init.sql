-- ----------------------------
-- 初始数据：
-- 1.生成基本栏目
-- ----------------------------
INSERT INTO `blog_category` VALUES ('1', '校园新闻', '0', null, '2015-09-18 08:21:57', '2015-09-18 08:21:57', '1');
INSERT INTO `blog_category` VALUES ('2', '校园生活', '0', null, '2015-09-18 08:21:48', '2015-09-18 08:21:48', '1');
INSERT INTO `blog_category` VALUES ('3', '博客', '0', null, '2015-09-18 08:15:00', '2015-09-18 08:11:52', '1');
INSERT INTO `blog_category` VALUES ('4', '物业公告', '0', null, '2015-09-18 08:22:09', '2015-09-18 08:22:09', '1');

-- ----------------------------
-- 初始数据：
-- 应用信息
-- ----------------------------
INSERT INTO `luyasi-flask`.`security_app` (`id`, `name`, `update_at`, `create_at`, `version`, `app_version`, `app_vercode`, `update_url`) VALUES ('1', 'dxc', NULL, NULL, '1', '1.0.0', '100', NULL);
