/*
Navicat SQLite Data Transfer

Source Server         : luyasi_flask
Source Server Version : 30714
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30714
File Encoding         : 65001

Date: 2013-12-26 17:52:05
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for qingbank_contact
-- ----------------------------
DROP TABLE IF EXISTS "main"."qingbank_contact";
CREATE TABLE qingbank_contact (
	id INTEGER NOT NULL, 
	employee_no VARCHAR(10), 
	name VARCHAR(10), 
	name_pinyin VARCHAR(30), 
	name_shot VARCHAR(10), 
	duty VARCHAR(10), 
	mobile VARCHAR(14), 
	telephone VARCHAR(20), 
	innerphone VARCHAR(20), 
	fax VARCHAR(14), 
	qq VARCHAR(20), 
	department_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(department_id) REFERENCES qingbank_department (id)
);

-- ----------------------------
-- Records of qingbank_contact
-- ----------------------------
INSERT INTO "main"."qingbank_contact" VALUES (1, '', '刘辛元', 'liuxinyuan', 'lxy', '董事长', '', 3868726, 833, 3868589, '', 1);
INSERT INTO "main"."qingbank_contact" VALUES (2, '', '黄振邦', 'huangzhenbang', 'hzb', '行长', '', 3868722, 831, 3868589, '', 1);
INSERT INTO "main"."qingbank_contact" VALUES (3, '', '姚能顺', 'yaonengshun', 'yns', '监事长', '', 3868725, 832, 3868589, '', 1);
INSERT INTO "main"."qingbank_contact" VALUES (4, '', '王德祥', 'wangdexiang', 'wdx', '副行长', '', 3869920, 814, 3868589, '', 1);
INSERT INTO "main"."qingbank_contact" VALUES (5, '', '于翔', 'yuxiang', 'yx', '副行长', '', 3868730, 835, 3868589, '', 1);
INSERT INTO "main"."qingbank_contact" VALUES (6, '', '王合贵', 'wanghegui', 'whg', '副总经理（主持工作）', 13631083977, 3868871, 840, 3868589, '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (7, '', '李媛', 'liyuan', 'ly', '总经理助理', 13922559683, 3868951, 837, 3868589, '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (8, '', '江瑶', 'jiangyao', 'jy', '副经理', 13824926556, 3868951, 837, 3868589, '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (9, '', '洪天带', 'hongtiandai', 'htd', '办事员', 13926613319, 3868951, 837, 3868589, '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (10, '', '杨迎虹', 'yangyinghong', 'yyh', '办事员', 15915176578, 3868951, 837, 3868589, '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (11, '', '张锐华', 'zhangruihua', 'zrh', '办事员', 15807650018, 3868951, 837, 3868589, '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (12, '', '刘清', 'liuqing', 'lq', '办事员', 13927625087, 3868951, 837, 3868589, '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (13, '', '陈玄', 'chenxuan', 'cx', '办事员', 13326551628, '', '', '', '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (14, '', '李丽仪', 'liliyi', 'lly', '办事员', 13509269059, '', '', '', '', 2);
INSERT INTO "main"."qingbank_contact" VALUES (15, '', '姜远秋', 'jiangyuanqiu', 'jyq', '副总经理（主持工作）', 13922560870, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (16, '', '潘贯虹', 'panguanhong', 'pgh', '总经理助理', 13926667693, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (17, '', '孙涛', 'suntao', 'st', '经理助理', 13413526883, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (18, '', '周阳春', 'zhouyangchun', 'zyc', '办事员', 13828505599, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (19, '', '申禀杰', 'shenbingjie', 'sbj', '办事员', 13922609811, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (20, '', '梁品彰', 'liangpinzhang', 'lpz', '办事员', 13922601862, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (21, '', '郭金洪', 'guojinhong', 'gjh', '司机', 13922603821, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (22, '', '罗锡钳', 'luoxiqian', 'lxq', '司机', 13926673376, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (23, '', '黄伙荣', 'huanghuorong', 'hhr', '司机', 13922606250, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (24, '', '吴伟军', 'wuweijun', 'wwj', '司机', 13808820161, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (25, '', '谭志斌', 'tanzhibin', 'tzb', '司机', 13828500586, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (26, '', '刘伯安', 'liuboan', 'lba', '司机', 13926673928, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (27, '', '丘文驱', 'qiuwenqu', 'qwq', '司机', 13902243849, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (28, '', '郑敏杰', 'zhengminjie', 'zmj', '司机', 15992043883, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (29, '', '陈云健', 'chenyunjian', 'cyj', '电工', 13413517355, 3869817, 816, '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (30, '', '李羚玉', 'lilingyu', 'lly', '接待员', 13416129621, '', '', '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (31, '', '朱东梅', 'zhudongmei', 'zdm', '清洁员', 15975854773, '', '', '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (32, '', '向燕霞', 'xiangyanxia', 'xyx', '清洁员', 13178494826, '', '', '', '', 3);
INSERT INTO "main"."qingbank_contact" VALUES (33, '', '李志辉', 'lizhihui', 'lzh', '副总经理（主持工作）', 13802896601, 3813702, '', 3813283, '', 4);
INSERT INTO "main"."qingbank_contact" VALUES (34, '', '杨灵锋', 'yanglingfeng', 'ylf', '副经理', 13926689570, 3868951, 837, 3868589, '', 4);
INSERT INTO "main"."qingbank_contact" VALUES (35, '', '赵汝炎', 'zhaoruyan', 'zry', '', 18826611111, 3868951, 837, 3868589, '', 4);
INSERT INTO "main"."qingbank_contact" VALUES (36, '', '陈国华', 'chenguohua', 'cgh', '', 13926600133, 3868951, 837, 3868589, '', 4);
INSERT INTO "main"."qingbank_contact" VALUES (37, '', '李利平', 'liliping', 'llp', '副总经理（主持工作）', 13828548636, 3868952, 838, 3868589, '', 5);
INSERT INTO "main"."qingbank_contact" VALUES (38, '', '邹毅', 'zouyi', 'zy', '副总经理', 13927667503, 3868952, 838, 3868589, '', 5);
INSERT INTO "main"."qingbank_contact" VALUES (39, '', '李秀茹', 'lixiuru', 'lxr', '副经理', 13602933902, 3868952, 838, 3868589, '', 5);
INSERT INTO "main"."qingbank_contact" VALUES (40, '', '谭海丽', 'tanhaili', 'thl', '副经理', 13288925786, 3868952, 838, 3868589, '', 5);
INSERT INTO "main"."qingbank_contact" VALUES (41, '', '邱有彦', 'qiuyouyan', 'qyy', '办事员', 13602949230, 3868952, 838, 3868589, '', 5);
INSERT INTO "main"."qingbank_contact" VALUES (42, '', '黄彦欣', 'huangyanxin', 'hyx', '办事员', 15992058375, 3868952, 838, 3868589, '', 5);
INSERT INTO "main"."qingbank_contact" VALUES (43, '', '钟小艳', 'zhongxiaoyan', 'zxy', '大堂经理', 15992006639, 3868952, 838, 3868589, '', 5);
INSERT INTO "main"."qingbank_contact" VALUES (44, '', '万烨', 'wanye', 'wy', '副总经理（主持工作）', 13926663706, 3869392, 822, 3869827, '', 6);
INSERT INTO "main"."qingbank_contact" VALUES (45, '', '刘升威', 'liushengwei', 'lsw', '总经理助理', 13824484528, 3869392, 822, 3869827, '', 6);
INSERT INTO "main"."qingbank_contact" VALUES (46, '', '李黎', 'lili', 'll', '副经理', 13828556481, 3869392, 822, 3869827, '', 6);
INSERT INTO "main"."qingbank_contact" VALUES (47, '', '潘子鸣', 'panziming', 'pzm', '办事员', 13509264299, 3869392, 822, 3869827, '', 6);
INSERT INTO "main"."qingbank_contact" VALUES (48, '', '程俊仪', 'chengjunyi', 'cjy', '办事员', 15007644661, 3869392, 822, 3869827, '', 6);
INSERT INTO "main"."qingbank_contact" VALUES (49, '', '蔡迎春', 'caiyingchun', 'cyc', '副总经理（主持工作）', 13926059116, 3868809, 809, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (50, '', '詹全鑫', 'zhanquanxin', 'zqx', '总经理助理', 13926669093, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (51, '', '罗贵君', 'luoguijun', 'lgj', '总经理助理', 13828545606, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (52, '', '邵文绚', 'shaowenxuan', 'swx', '经理助理', 13610573812, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (53, '', '翟光磊', 'diguanglei', 'dgl', '办事员', 13927602767, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (54, '', '牛冬梅', 'niudongmei', 'ndm', '办事员', 15989100706, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (55, '', '林应龙', 'linyinglong', 'lyl', '办事员', 13926645450, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (56, '', '邝凡帆', 'kuangfanfan', 'kff', '办事员', 13620536373, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (57, '', '叶梅娇', 'yemeijiao', 'ymj', '办事员', 13802891835, 3868821, 882, 3868419, '', 7);
INSERT INTO "main"."qingbank_contact" VALUES (58, '', '俞俊英', 'yujunying', 'yjy', '副总经理（主持工作）', 13802896561, 3869837, 825, 3869837, '', 8);
INSERT INTO "main"."qingbank_contact" VALUES (59, '', '梁海波', 'lianghaibo', 'lhb', '副总经理', 13927621260, 3869837, 825, 3869837, '', 8);
INSERT INTO "main"."qingbank_contact" VALUES (60, '', '何敏彩', 'hemincai', 'hmc', '总经理助理', 13922602167, 3869837, 825, 3869837, '', 8);
INSERT INTO "main"."qingbank_contact" VALUES (61, '', '钟玉勤', 'zhongyuqin', 'zyq', '经理', 13927639889, 3869837, 825, 3869837, '', 8);
INSERT INTO "main"."qingbank_contact" VALUES (62, '', '罗文艳', 'luowenyan', 'lwy', '办事员', 13415220011, 3869837, 825, 3869837, '', 8);
INSERT INTO "main"."qingbank_contact" VALUES (63, '', '侯淑华', 'houshuhua', 'hsh', '办事员', 13416564662, 3869837, 825, 3869837, '', 8);
INSERT INTO "main"."qingbank_contact" VALUES (64, '', '阮静文', 'ruanjingwen', 'rjw', '经理助理', 15975844592, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (65, '', '刘莹莹', 'liuyingying', 'lyy', '办事员', 18023733922, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (66, '', '罗小勤', 'luoxiaoqin', 'lxq', '办事员', 13927689068, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (67, '', '成丽梅', 'chenglimei', 'clm', '办事员', 13824938016, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (68, '', '黄惠敏', 'huanghuimin', 'hhm', '办事员', 13727100886, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (69, '', '赖君带', 'laijundai', 'ljd', '办事员', 13415294568, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (70, '', '黄洁洁', 'huangjiji', 'hjj', '办事员', 13802894833, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (71, '', '梁彩金', 'liangcaijin', 'lcj', '办事员', 13727151188, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (72, '', '李丽娟', 'lilijuan', 'llj', '办事员', 13927689613, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (73, '', '徐家宝', 'xujiabao', 'xjb', '办事员', 18666697930, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (74, '', '蔡明智', 'caimingzhi', 'cmz', '办事员', 13828566200, 3868956, 828, '', '', 9);
INSERT INTO "main"."qingbank_contact" VALUES (75, '', '姚碧霞', 'yaobixia', 'ybx', '办事员', 13539529833, 3869732, 812, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (76, '', '吴剑华', 'wujianhua', 'wjh', '办事员', 13602946966, 3869732, 812, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (77, '', '廖海梅', 'liaohaimei', 'lhm', '办事员', 13924422898, 3869732, 812, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (78, '', '梁文艳', 'liangwenyan', 'lwy', '办事员', 13926684664, 3869732, 812, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (79, '', '何瑞仪', 'heruiyi', 'hry', '办事员', 13750192257, 3869732, 812, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (80, '', '郑美凤', 'zhengmeifeng', 'zmf', '办事员', 13926619200, 3869732, 812, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (81, '', '陈志丽', 'chenzhili', 'czl', '办事员', 13927629223, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (82, '', '张利军', 'zhanglijun', 'zlj', '办事员', 13926689824, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (83, '', '潘雪文', 'panxuewen', 'pxw', '办事员', 13924411501, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (84, '', '黄毅胜', 'huangyisheng', 'hys', '办事员', 13727117011, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (85, '', '卢玉其', 'luyuqi', 'lyq', '办事员', 13553948717, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (86, '', '赵劲华', 'zhaojinghua', 'zjh', '办事员', 13509263140, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (87, '', '温建权', 'wenjianquan', 'wjq', '办事员', 13926686028, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (88, '', '郑子荣', 'zhengzirong', 'zzr', '办事员', 13926680999, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (89, '', '刘势华', 'liushihua', 'lsh', '办事员', 15107653239, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (90, '', '叶杰明', 'yejieming', 'yjm', '办事员', 13509268647, 3868476, 818, '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (91, '', '梁丽卿', 'liangliqing', 'llq', '办事员', 13922608213, 3869817, '', '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (92, '', '刘永洪', 'liuyonghong', 'lyh', '办事员', 13802890075, 3869817, '', '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (93, '', '谭杏和', 'tanxinghe', 'txh', '办事员', 13509261098, 3869817, '', '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (94, '', '钟有群', 'zhongyouqun', 'zyq', '办事员', 13729606478, 3869817, '', '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (95, '', '冯小华', 'fengxiaohua', 'fxh', '办事员', 13542493078, 3869817, '', '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (96, '', '刘玉明', 'liuyuming', 'lym', '办事员', 13926647863, 3869817, '', '', '', 10);
INSERT INTO "main"."qingbank_contact" VALUES (97, '', '刘大健', 'liudajian', 'ldj', '副总经理（主持工作）', 13926686448, 3869358, 826, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (98, '', '肖浩培', 'xiaohaopei', 'xhp', '经理', 13926667050, 3869358, 826, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (99, '', '文  勇', 'wen  yong', 'w  y', '金融护卫人员', 13927682036, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (100, '', '谢展华', 'xiezhanhua', 'xzh', '金融护卫人员', 13610596789, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (101, '', '汤锐洪', 'tangruihong', 'trh', '金融护卫人员', 13602933440, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (102, '', '徐伟明', 'xuweiming', 'xwm', '金融护卫人员', 13602933403, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (103, '', '郭锦新', 'guojinxin', 'gjx', '金融护卫人员', 13417256722, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (104, '', '潘国标', 'panguobiao', 'pgb', '金融护卫人员', 13553920332, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (105, '', '潘文康', 'panwenkang', 'pwk', '金融护卫人员', 13729681629, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (106, '', '黄镜明', 'huangjingming', 'hjm', '金融护卫人员', 18922603606, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (107, '', '朱荣桂', 'zhuronggui', 'zrg', '金融护卫人员', 13431984898, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (108, '', '彭炳灿', 'pengbingcan', 'pbc', '金融护卫人员', 15915116838, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (109, '', '梁少明', 'liangshaoming', 'lsm', '金融护卫人员', 13631071303, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (110, '', '林志坚', 'linzhijian', 'lzj', '金融护卫人员', 13926688809, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (111, '', '梁健初', 'liangjianchu', 'ljc', '金融护卫人员', 13750168730, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (112, '', '黄国坚', 'huangguojian', 'hgj', '金融护卫人员', 13435259501, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (113, '', '范志煌', 'fanzhihuang', 'fzh', '金融护卫人员', 15917504745, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (114, '', '陈佳伟', 'chenjiawei', 'cjw', '金融护卫人员', 13926616683, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (115, '', '郑燕彬', 'zhengyanbin', 'zyb', '金融护卫人员', 13679533866, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (116, '', '王小兵', 'wangxiaobing', 'wxb', '金融护卫人员', 13828559308, 3868667, 827, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (117, '', '宋文勇', 'songwenyong', 'swy', '解钞车司机', 15218522298, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (118, '', '谢锦添', 'xiejintian', 'xjt', '解钞车司机', 13926673422, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (119, '', '汤雪江', 'tangxuejiang', 'txj', '解钞车司机', 13539500446, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (120, '', '谭玉明', 'tanyuming', 'tym', '解钞车司机', 13729681678, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (121, '', '陈嘉荣', 'chenjiarong', 'cjr', '解钞车司机', 13927667908, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (122, '', '林海新', 'linhaixin', 'lhx', '解钞车司机', 13802896781, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (123, '', '刘伟业', 'liuweiye', 'lwy', '解钞车司机', 13828507288, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (124, '', '汤汝光', 'tangruguang', 'trg', '总行远程监控中心', 13729658416, 3869967, '', '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (125, '', '潘  伟', 'pan  wei', 'p  w', '总行远程监控中心', 15992043232, 3869967, '', '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (126, '', '吴俊生', 'wujunsheng', 'wjs', '总行远程监控中心', 13679542322, 3869967, '', '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (127, '', '梁志定', 'liangzhiding', 'lzd', '总行远程监控中心', 13802899139, 3869967, '', '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (128, '', '欧国杰', 'ouguojie', 'ogj', '总行远程监控中心', 18200603832, 3869967, '', '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (129, '', '蔡晓凡', 'caixiaofan', 'cxf', '总行远程监控中心', 13610503311, 3869967, '', '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (130, '', '柳志勇', 'liuzhiyong', 'lzy', '总行保安员（劳务派遣）', 13610525546, 3869817, 816, '', '', 11);
INSERT INTO "main"."qingbank_contact" VALUES (131, '', '余少荣', 'yushaorong', 'ysr', '总经理', 13602935221, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (132, '', '苏瑞锋', 'suruifeng', 'srf', '副总经理', 13922605686, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (133, '', '薛锦华', 'xuejinhua', 'xjh', '副经理', 13927693880, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (134, '', '陈  姗', 'chen  shan', 'c  s', '经理助理', 13535969815, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (135, '', '徐小梅', 'xuxiaomei', 'xxm', '稽核岗', 13922607505, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (136, '', '郑碧婷', 'zhengbiting', 'zbt', '纪检监察岗', 13750151599, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (137, '', '韦碧丹', 'weibidan', 'wbd', '派驻稽核员', 13927622187, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (138, '', '戚文泳', 'qiwenyong', 'qwy', '审计岗', 18926699920, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (139, '', '王  迅', 'wang  xun', 'w  x', '派驻稽核员', 13926665853, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (140, '', '关洁琳', 'guanjilin', 'gjl', '派驻稽核员', 13924411763, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (141, '', '华金兰', 'huajinlan', 'hjl', '派驻稽核员', 15876300554, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (142, '', '陈  彦', 'chen  yan', 'c  y', '派驻稽核员', 13417237054, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (143, '', '向伟杰', 'xiangweijie', 'xwj', '派驻稽核员', 13922601419, 3813238, '', '', '', 12);
INSERT INTO "main"."qingbank_contact" VALUES (144, '', '何啟星', 'heqixing', 'hqx', '副总经理（主持工作）', 13828566922, 3869807, 823, '', '', 13);
INSERT INTO "main"."qingbank_contact" VALUES (145, '', '冯瀚文', 'fenghanwen', 'fhw', '经理', 18666692611, 3869807, 823, '', '', 13);
INSERT INTO "main"."qingbank_contact" VALUES (146, '', '潘雪颜', 'panxueyan', 'pxy', '反洗钱岗', 13802890660, 3869807, 823, '', '', 13);
INSERT INTO "main"."qingbank_contact" VALUES (147, '', '黄烜', 'huangxuan', 'hx', '副总经理（主持工作）', 13824947799, 3813878, '', '', '', 14);
INSERT INTO "main"."qingbank_contact" VALUES (148, '', '薛爱云', 'xueaiyun', 'xay', '经理助理', 13926661685, 3813878, '', '', '', 14);
INSERT INTO "main"."qingbank_contact" VALUES (149, '', '卢沛勋', 'lupeixun', 'lpx', '客户经理', 13501469227, 3813878, '', '', '', 14);
INSERT INTO "main"."qingbank_contact" VALUES (150, '', '李桂潮', 'liguichao', 'lgc', '客户经理', 13828507992, 3813878, '', '', '', 14);
INSERT INTO "main"."qingbank_contact" VALUES (151, '', '彭永亮', 'pengyongliang', 'pyl', '客户经理', 13542466566, 3813878, '', '', '', 14);
INSERT INTO "main"."qingbank_contact" VALUES (152, '', '罗国宇', 'luoguoyu', 'lgy', '副总经理（主持工作）', 13824948899, 3868871, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (153, '', '张红军', 'zhanghongjun', 'zhj', '总经理助理', 13926662549, 3868871, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (154, '', '黎惠贞', 'lihuizhen', 'lhz', '总经理助理', 13922557133, 3868871, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (155, '', '陈  凯', 'chen  kai', 'c  k', '总经理助理', 13828569851, 3869329, 821, '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (156, '', '苏国毅', 'suguoyi', 'sgy', '经理', 13927621477, 3813732, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (157, '', '张娈', 'zhangluan', 'zl', '经理助理', 13926671560, '', '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (158, '', '钟健文', 'zhongjianwen', 'zjw', '贷审员', 13750166848, 3813732, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (159, '', '陈瑞光', 'chenruiguang', 'crg', '贷审员', 13602942500, 3869329, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (160, '', '郑海燕', 'zhenghaiyan', 'zhy', '贷审员', 13922604303, 3813732, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (161, '', '韦宇劲', 'weiyujing', 'wyj', '贷审员', 18675670867, 3813732, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (162, '', '黄  藜', 'huang  li', 'h  l', '调统员', 13926679519, 3869329, 821, '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (163, '', '蔡雅静', 'caiyajing', 'cyj', '贷审员', 13750183332, 3869329, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (164, '', '郑广强', 'zhengguangqiang', 'zgq', '贷审员', 13828579332, '', '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (165, '', '温伟明', 'wenweiming', 'wwm', '贷审员', 13828509376, 3813732, '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (166, '', '周兴胜', 'zhouxingsheng', 'zxs', '贷审员', 13927627976, '', '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (167, '', '杨恒', 'yangheng', 'yh', '贷审员', 13824926988, '', '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (168, '', '陈文婷', 'chenwenting', 'cwt', '', 13922607606, '', '', '', '', 15);
INSERT INTO "main"."qingbank_contact" VALUES (169, '', '刘锡辉', 'liuxihui', 'lxh', '副总经理（主持工作）', 13500298722, 3813118, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (170, '', '冼强', 'xianqiang', 'xq', '总经理助理', 13927681515, 3813318, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (171, '', '郑保存', 'zhengbaocun', 'zbc', '总经理助理', 13828534711, 3813318, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (172, '', '梁桂新', 'liangguixin', 'lgx', '经理', 13602944429, 3813318, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (173, '', '潘丽华', 'panlihua', 'plh', '经理助理', 13824921314, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (174, '', '张琛', 'zhangchen', 'zc', '客户经理', 13926671530, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (175, '', '梁珊珊', 'liangshanshan', 'lss', '客户经理', 13509262036, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (176, '', '任卓', 'renzhuo', 'rz', '客户经理', 13927676822, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (177, '', '胡玲琳', 'hulinglin', 'hll', '业务经理', 13922610160, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (178, '', '刘岚岚', 'liulanlan', 'lll', '客户经理', 13926669356, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (179, '', '陈雪慧', 'chenxuehui', 'cxh', '客户经理', 13926685529, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (180, '', '吕鸿鳅', 'lvhongqiu', 'lhq', '客户经理', 13802898927, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (181, '', '王嘉健', 'wangjiajian', 'wjj', '客户经理', 13413537309, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (182, '', '郭亦思', 'guoyisi', 'gys', '业务经理', 18998613111, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (183, '', '黄绮珊', 'huangqishan', 'hqs', '综合岗', 13413525525, 3813388, '', 3813121, '', 16);
INSERT INTO "main"."qingbank_contact" VALUES (184, '', '韩飞', 'hanfei', 'hf', '副总经理（主持工作）', 13322817951, 3869905, 824, 3868419, '', 17);
INSERT INTO "main"."qingbank_contact" VALUES (185, '', '袁慧靖', 'yuanhuijing', 'yhj', '副经理', 13500298557, 3869915, 830, 3868419, '', 17);
INSERT INTO "main"."qingbank_contact" VALUES (186, '', '徐秋怡', 'xuqiuyi', 'xqy', '经理助理', 13926677617, 3869915, 830, 3868419, '', 17);
INSERT INTO "main"."qingbank_contact" VALUES (187, '', '龙祥案', 'longxiangan', 'lxa', '产品经理', 13927635998, 3869915, 830, 3868419, '', 17);
INSERT INTO "main"."qingbank_contact" VALUES (188, '', '赵盼', 'zhaopan', 'zp', '产品经理', 13726974576, 3869329, 821, 3868419, '', 17);
INSERT INTO "main"."qingbank_contact" VALUES (189, '', '梁锦山', 'liangjinshan', 'ljs', '产品经理', 13602946040, 3869329, 821, 3868419, '', 17);
INSERT INTO "main"."qingbank_contact" VALUES (190, '', '王盈盈', 'wangyingying', 'wyy', '文员', 13059586066, 3869915, 830, 3868419, '', 17);
INSERT INTO "main"."qingbank_contact" VALUES (191, '', '张伟钊', 'zhangweizhao', 'zwz', '副总经理（主持工作）', 13802890718, 3869905, 824, 3868419, '', 18);
INSERT INTO "main"."qingbank_contact" VALUES (192, '', '倪晖', 'nihui', 'nh', '总经理助理', 13509265222, 3868551, 836, 3868419, '', 18);
INSERT INTO "main"."qingbank_contact" VALUES (193, '', '黄丽琴', 'huangliqin', 'hlq', '经理助理', 13926670345, 3868551, 836, 3868419, '', 18);
INSERT INTO "main"."qingbank_contact" VALUES (194, '', '朱石柱', 'zhushizhu', 'zsz', '客户经理', 13824926984, 3868551, 836, 3868419, '', 18);
INSERT INTO "main"."qingbank_contact" VALUES (195, '', '郭倩妮', 'guoqianni', 'gqn', '客户经理', 13926644162, 3868551, 836, 3868419, '', 18);
INSERT INTO "main"."qingbank_contact" VALUES (196, '', '黄韶伟', 'huangshaowei', 'hsw', '文员', 13802896559, 3868551, 836, 3868419, '', 18);
INSERT INTO "main"."qingbank_contact" VALUES (197, '', '李志辉', 'lizhihui', 'lzh', '副总经理（主持工作）', 13802896601, 3813702, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (198, '', '林伟文', 'linweiwen', 'lww', '经理', 13750182628, 3813283, '', 3813283, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (199, '', '徐灿洪', 'xucanhong', 'xch', '经理', 13926666449, 3813283, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (200, '', '张玮', 'zhangwei', 'zw', '副经理', 13828556884, 3813283, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (201, '', '陈旭新', 'chenxuxin', 'cxx', '办事员', 13926683158, 3813232, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (202, '', '蔡思华', 'caisihua', 'csh', '办事员', 13927693838, 3875938, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (203, '', '欧舒韵', 'oushuyun', 'osy', '办事员', 13926647177, 3813232, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (204, '', '龙粤君', 'longyuejun', 'lyj', '办事员', 13922606635, 3875938, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (205, '', '潘婉莹', 'panwanying', 'pwy', '办事员', 13926645845, 3875938, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (206, '', '卢艳梅', 'luyanmei', 'lym', '办事员', 13750191123, 3875938, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (207, '', '刘伟航', 'liuweihang', 'lwh', '办事员', 15813267232, 3813232, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (208, '', '李卫忠', 'liweizhong', 'lwz', '办事员', 13602935554, 3813232, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (209, '', '刘纯瑗', 'liuchunyuan', 'lcy', '文员', 13926664200, 3813263, '', 3813263, '', 19);
INSERT INTO "main"."qingbank_contact" VALUES (210, '', '肖国初', 'xiaoguochu', 'xgc', '副总经理（主持工作）', 13922603878, 3969883, 813, 3869921, '', 20);
INSERT INTO "main"."qingbank_contact" VALUES (211, '', '钟敬', 'zhongjing', 'zj', '总经理助理', 13500297004, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (212, '', '宋锦明', 'songjinming', 'sjm', '经理', '15019338146     13824928131', 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (213, '', '汤浩锋', 'tanghaofeng', 'thf', '经理助理', 13828559004, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (214, '', '徐海锋', 'xuhaifeng', 'xhf', '客户经理', 13802890267, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (215, '', '梁永健', 'liangyongjian', 'lyj', '客户经理', 13926683817, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (216, '', '罗炳强', 'luobingqiang', 'lbq', '客户经理', 13926685025, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (217, '', '廖卫东', 'liaoweidong', 'lwd', '客户经理', 13926658813, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (218, '', '龚晓文', 'gongxiaowen', 'gxw', '客户经理', 13750148850, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (219, '', '高鹏晓', 'gaopengxiao', 'gpx', '客户经理', 13926682082, 3869921, 820, 3869921, '', 21);
INSERT INTO "main"."qingbank_contact" VALUES (220, '', '谢春志', 'xiechunzhi', 'xcz', '办事员', 13926683986, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (221, '', '聂柳芬', 'nieliufen', 'nlf', '办事员', 15382956066, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (222, '', '王晓倩', 'wangxiaoqian', 'wxq', '办事员', 13926682829, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (223, '', '李秋敏', 'liqiumin', 'lqm', '办事员', 13610506018, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (224, '', '廖家敏', 'liaojiamin', 'ljm', '办事员', 15811726712, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (225, '', '柳海玉', 'liuhaiyu', 'lhy', '办事员', 13926612772, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (226, '', '胡志坚', 'huzhijian', 'hzj', '办事员', 13425229009, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (227, '', '陈婉婷', 'chenwanting', 'cwt', '办事员', 13727120616, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (228, '', '周文倩', 'zhouwenqian', 'zwq', '办事员', 13542469491, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (229, '', '叶思静', 'yesijing', 'ysj', '办事员', 13727127541, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (230, '', '苏甄', 'suzhen', 'sz', '办事员', 13413526115, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (231, '', '叶顺霞', 'yeshunxia', 'ysx', '办事员', 13413454883, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (232, '', '罗缨媚', 'luoyingmei', 'lym', '办事员', 13535997722, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (233, '', '梁玉玲', 'liangyuling', 'lyl', '办事员', 13922608997, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (234, '', '朱艺琳', 'zhuyilin', 'zyl', '办事员', 13924413166, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (235, '', '李鸣宇', 'limingyu', 'lmy', '办事员', 13380712621, 3869731, 811, 3869921, '', 22);
INSERT INTO "main"."qingbank_contact" VALUES (236, '', '侯志伟', 'houzhiwei', 'hzw', '行长', 13631088099, 3393399, '', '', '', 23);
INSERT INTO "main"."qingbank_contact" VALUES (237, '', '汤庆文', 'tangqingwen', 'tqw', '行长助理', 13824941898, 3311083, '', '', '', 23);
INSERT INTO "main"."qingbank_contact" VALUES (238, '', '何翠珍', 'hecuizhen', 'hcz', '行长助理', 13926661996, 3311083, '', '', '', 23);
INSERT INTO "main"."qingbank_contact" VALUES (239, '', '罗勇坚', 'luoyongjian', 'lyj', '中级客户经理', 13602935675, 3311083, '', '', '', 24);
INSERT INTO "main"."qingbank_contact" VALUES (240, '', '谢宇海', 'xieyuhai', 'xyh', '信贷主管', 13828529866, 3393355, '', '', '', 24);
INSERT INTO "main"."qingbank_contact" VALUES (241, '', '侯泳甜', 'houyongtian', 'hyt', '客户经理', 13680009335, 3393355, '', '', '', 24);
INSERT INTO "main"."qingbank_contact" VALUES (242, '', '刘勇劲', 'liuyongjing', 'lyj', '客户经理', 15807642342, 3393355, '', '', '', 24);
INSERT INTO "main"."qingbank_contact" VALUES (243, '', '赖文有', 'laiwenyou', 'lwy', '客户经理', 15303027348, 3393355, '', '', '', 24);
INSERT INTO "main"."qingbank_contact" VALUES (244, '', '廖键伟', 'liaojianwei', 'ljw', '客户经理', 13926662071, 3393355, '', '', '', 24);
INSERT INTO "main"."qingbank_contact" VALUES (245, '', '练庆焕', 'lianqinghuan', 'lqh', '办事员', 15813266287, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (246, '', '李建容', 'lijianrong', 'ljr', '办事员', 13417292163, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (247, '', '郭钟灵', 'guozhongling', 'gzl', '办事员', 15816248530, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (248, '', '刘玉仪', 'liuyuyi', 'lyy', '办事员', 13542488601, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (249, '', '陈楚璇', 'chenchuxuan', 'ccx', '办事员', 15917600864, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (250, '', '朱毅刚', 'zhuyigang', 'zyg', '办事员', 18826608266, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (251, '', '邓颖怡', 'dengyingyi', 'dyy', '办事员', 13927682608, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (252, '', '黄燕燕', 'huangyanyan', 'hyy', '柜台主管', 13927689019, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (253, '', '刘国仪', 'liuguoyi', 'lgy', '办事员', 13729635730, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (254, '', '张锐华', 'zhangruihua', 'zrh', '办事员', 15807650018, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (255, '', '李志勇', 'lizhiyong', 'lzy', '办事员', 13553987282, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (256, '', '温斯慧', 'wensihui', 'wsh', '办事员', 13413523827, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (257, '', '何春宜', 'hechunyi', 'hcy', '大堂经理', 13922602939, 3393311, '', 3393311, '', 25);
INSERT INTO "main"."qingbank_contact" VALUES (258, '', '冯静君', 'fengjingjun', 'fjj', '经理助理', 13824920007, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (259, '', '林玉霞', 'linyuxia', 'lyx', '柜台主管', 13927661032, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (260, '', '凃颖', 'tuying', 'ty', '办事员', 15119969429, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (261, '', '谢惠群', 'xiehuiqun', 'xhq', '办事员', 13417270246, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (262, '', '彭燕飞', 'pengyanfei', 'pyf', '办事员', 13425210718, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (263, '', '侯洁玲', 'houjiling', 'hjl', '办事员', 15992005321, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (264, '', '罗家杰', 'luojiajie', 'ljj', '办事员', 13926688465, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (265, '', '李洁玲', 'lijiling', 'ljl', '大堂经理', 15914983007, 3337013, '', '', '', 26);
INSERT INTO "main"."qingbank_contact" VALUES (266, '', '林海玲', 'linhailing', 'lhl', '经理助理', 13726985880, 3311661, '', '', '', 27);
INSERT INTO "main"."qingbank_contact" VALUES (267, '', '何秋婵', 'heqiuchan', 'hqc', '柜台主管', 13922605698, 3311661, '', '', '', 27);
INSERT INTO "main"."qingbank_contact" VALUES (268, '', '柯伟东', 'keweidong', 'kwd', '办事员', 13622439061, 3311661, '', '', '', 27);
INSERT INTO "main"."qingbank_contact" VALUES (269, '', '郑洁明', 'zhengjiming', 'zjm', '办事员', 13927626655, 3311661, '', '', '', 27);
INSERT INTO "main"."qingbank_contact" VALUES (270, '', '黄文军', 'huangwenjun', 'hwj', '办事员', 13620570755, 3311661, '', '', '', 27);
INSERT INTO "main"."qingbank_contact" VALUES (271, '', '杨丽芬', 'yanglifen', 'ylf', '办事员', 15019312398, 3311661, '', '', '', 27);
INSERT INTO "main"."qingbank_contact" VALUES (272, '', '林玉芬', 'linyufen', 'lyf', '大堂经理', 13417259138, 3311661, '', '', '', 27);
INSERT INTO "main"."qingbank_contact" VALUES (273, '', '梁燕娜', 'liangyannuo', 'lyn', '经理助理', 13924411649, 3327163, '', '', '', 28);
INSERT INTO "main"."qingbank_contact" VALUES (274, '', '朱永光', 'zhuyongguang', 'zyg', '办事员', 13509268032, 3327163, '', '', '', 28);
INSERT INTO "main"."qingbank_contact" VALUES (275, '', '罗卫勤', 'luoweiqin', 'lwq', '办事员', 13553963500, 3327163, '', '', '', 28);
INSERT INTO "main"."qingbank_contact" VALUES (276, '', '汤树森', 'tangshusen', 'tss', '办事员', 18926636933, 3327163, '', '', '', 28);
INSERT INTO "main"."qingbank_contact" VALUES (277, '', '陈瑞友', 'chenruiyou', 'cry', '经理助理', 13542497299, 3300538, '', '', '', 29);
INSERT INTO "main"."qingbank_contact" VALUES (278, '', '黎耀军', 'liyaojun', 'lyj', '柜台主管', 13927667263, 3300538, '', '', '', 29);
INSERT INTO "main"."qingbank_contact" VALUES (279, '', '李建红', 'lijianhong', 'ljh', '办事员', 13927682818, 3300538, '', '', '', 29);
INSERT INTO "main"."qingbank_contact" VALUES (280, '', '潘国清', 'panguoqing', 'pgq', '办事员', 13680002277, 3300538, '', '', '', 29);
INSERT INTO "main"."qingbank_contact" VALUES (281, '', '温燕清', 'wenyanqing', 'wyq', '办事员', 13509266551, 3300538, '', '', '', 29);
INSERT INTO "main"."qingbank_contact" VALUES (282, '', '白妍', 'baiyan', 'by', '经理助理', 13927665899, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (283, '', '谢献萍', 'xiexianping', 'xxp', '柜台主管', 13631069688, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (284, '', '邓志雄', 'dengzhixiong', 'dzx', '办事员', 13417278768, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (285, '', '邓顺怡', 'dengshunyi', 'dsy', '办事员', 13680005818, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (286, '', '孔梅英', 'kongmeiying', 'kmy', '办事员', 15876300728, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (287, '', '冯碧莹', 'fengbiying', 'fby', '办事员', 13926670905, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (288, '', '刘玉明', 'liuyuming', 'lym', '办事员', 13926647863, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (289, '', '罗文芳', 'luowenfang', 'lwf', '大堂经理', 15813250121, 3312983, '', '', '', 30);
INSERT INTO "main"."qingbank_contact" VALUES (290, '', '王艳', 'wangyan', 'wy', '经理助理', 13926663607, 3336060, '', '', '', 31);
INSERT INTO "main"."qingbank_contact" VALUES (291, '', '余建新', 'yujianxin', 'yjx', '办事员', 15975870806, 3336060, '', '', '', 31);
INSERT INTO "main"."qingbank_contact" VALUES (292, '', '梁素娟', 'liangsujuan', 'lsj', '办事员', 13926682622, 3336060, '', '', '', 31);
INSERT INTO "main"."qingbank_contact" VALUES (293, '', '刘达蕴', 'liudayun', 'ldy', '办事员', 15816286645, 3336060, '', '', '', 31);
INSERT INTO "main"."qingbank_contact" VALUES (294, '', '钱焕好', 'qianhuanhao', 'qhh', '办事员', 13602945268, 3336060, '', '', '', 31);
INSERT INTO "main"."qingbank_contact" VALUES (295, '', '陈晶晶', 'chenjingjing', 'cjj', '办事员', 13431955311, 3336060, '', '', '', 31);
INSERT INTO "main"."qingbank_contact" VALUES (296, '', '李安琪', 'lianqi', 'laq', '大堂经理', 13750159372, 3336060, '', '', '', 31);
INSERT INTO "main"."qingbank_contact" VALUES (297, '', '侯绍谦', 'houshaoqian', 'hsq', '行长', 13509262078, 3921208, '', '', '', 32);
INSERT INTO "main"."qingbank_contact" VALUES (298, '', '陈小文', 'chenxiaowen', 'cxw', '副行长', 13926688303, 3929966, '', '', '', 33);
INSERT INTO "main"."qingbank_contact" VALUES (299, '', '卢瑞红', 'luruihong', 'lrh', '行长助理', 13926673366, 3929966, '', '', '', 33);
INSERT INTO "main"."qingbank_contact" VALUES (300, '', '朱伟轩', 'zhuweixuan', 'zwx', '司机', 13802895229, 3924880, '', '', '', 34);
INSERT INTO "main"."qingbank_contact" VALUES (301, '', '汤银', 'tangyin', 'ty', '报帐员', 13413528766, 3924880, '', '', '', 34);
INSERT INTO "main"."qingbank_contact" VALUES (302, '', '潘彩霞', 'pancaixia', 'pcx', '信贷资料员', 13926673930, 3924880, '', '', '', 34);
INSERT INTO "main"."qingbank_contact" VALUES (303, '', '陈燮元', 'chenxieyuan', 'cxy', '信贷负责人', 15816298777, 3925763, '', '', '', 35);
INSERT INTO "main"."qingbank_contact" VALUES (304, '', '李启泉', 'liqiquan', 'lqq', '客户经理', 13927668070, 3925763, '', '', '', 35);
INSERT INTO "main"."qingbank_contact" VALUES (305, '', '余劲辉', 'yujinghui', 'yjh', '客户经理', 13926660204, 3925763, '', '', '', 35);
INSERT INTO "main"."qingbank_contact" VALUES (306, '', '邓毅贤', 'dengyixian', 'dyx', '客户经理', 13926672040, 3925763, '', '', '', 35);
INSERT INTO "main"."qingbank_contact" VALUES (307, '', '李枝中', 'lizhizhong', 'lzz', '客户经理', 13802892168, 3938313, '', '', '', 36);
INSERT INTO "main"."qingbank_contact" VALUES (308, '', '陈丽诗', 'chenlishi', 'cls', '客户经理', 13431999792, 3938313, '', '', '', 36);
INSERT INTO "main"."qingbank_contact" VALUES (309, '', '黄泽文', 'huangzewen', 'hzw', '客户经理', 13922563668, 3938313, '', '', '', 36);
INSERT INTO "main"."qingbank_contact" VALUES (310, '', '叶伟其', 'yeweiqi', 'ywq', '客户经理', 13922563663, 3938313, '', '', '', 36);
INSERT INTO "main"."qingbank_contact" VALUES (311, '', '黄国君', 'huangguojun', 'hgj', '客户经理', 13828555278, 3938313, '', '', '', 36);
INSERT INTO "main"."qingbank_contact" VALUES (312, '', '黄镜洪', 'huangjinghong', 'hjh', '客户经理', 13620580638, 3938313, '', '', '', 36);
INSERT INTO "main"."qingbank_contact" VALUES (313, '', '黄燕飞', 'huangyanfei', 'hyf', '负责人', 13417276675, 3921165, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (314, '', '罗金燕', 'luojinyan', 'ljy', '柜台主管', 13927663770, 3921165, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (315, '', '罗彩灵', 'luocailing', 'lcl', '柜员', 15813250738, 3921165, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (316, '', '钟国英', 'zhongguoying', 'zgy', '柜员', 13542460448, 3921165, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (317, '', '潘瑞平', 'panruiping', 'prp', '柜员', 13727112308, 3921165, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (318, '', '向晓婷', 'xiangxiaoting', 'xxt', '柜员', 13922603987, 3921165, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (319, '', '卢敬文', 'lujingwen', 'ljw', '柜员', 18933643382, 3921165, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (320, '', '林一楠', 'linyinan', 'lyn', '柜员', 13610586591, 3324006, '', 3921165, '', 37);
INSERT INTO "main"."qingbank_contact" VALUES (321, '', '成丽丽', 'chenglili', 'cll', '柜台主管', 13828509296, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (322, '', '刘丽军', 'liulijun', 'llj', '柜员', 13553949355, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (323, '', '何玉萍', 'heyuping', 'hyp', '柜员', 13926613906, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (324, '', '廖伟萍', 'liaoweiping', 'lwp', '柜员', 13553902330, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (325, '', '罗娴', 'luoxian', 'lx', '柜员', 13926688355, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (326, '', '张旭', 'zhangxu', 'zx', '柜员', 13926680170, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (327, '', '马晓阳', 'maxiaoyang', 'mxy', '柜员', 13226569896, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (328, '', '林玉香', 'linyuxiang', 'lyx', '柜员', 13413591936, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (329, '', '廖铭哲', 'liaomingzhe', 'lmz', '柜员', 13726989484, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (330, '', '陈雪洁', 'chenxueji', 'cxj', '柜员', 13926646002, 3928143, '', '', '', 38);
INSERT INTO "main"."qingbank_contact" VALUES (331, '', '许球知', 'xuqiuzhi', 'xqz', '网点负责人', 13927635556, 3324006, '', '', '', 39);
INSERT INTO "main"."qingbank_contact" VALUES (332, '', '黄志勤', 'huangzhiqin', 'hzq', '主管柜员', 13679501589, 3324006, '', '', '', 39);
INSERT INTO "main"."qingbank_contact" VALUES (333, '', '黄玉萍', 'huangyuping', 'hyp', '柜员', 13927669321, 3324006, '', '', '', 39);
INSERT INTO "main"."qingbank_contact" VALUES (334, '', '禤银弟', 'xuanyindi', 'xyd', '柜员', 13432701380, 3324006, '', '', '', 39);
INSERT INTO "main"."qingbank_contact" VALUES (335, '', '梁少珍', 'liangshaozhen', 'lsz', '柜员', 13729682686, 3324006, '', '', '', 39);
INSERT INTO "main"."qingbank_contact" VALUES (336, '', '许笑梅', 'xuxiaomei', 'xxm', '经理助理', 13828582211, 3315505, '', '', '', 40);
INSERT INTO "main"."qingbank_contact" VALUES (337, '', '赖洪初', 'laihongchu', 'lhc', '柜台主管', 13927621276, 3315505, '', '', '', 40);
INSERT INTO "main"."qingbank_contact" VALUES (338, '', '潘洪亮', 'panhongliang', 'phl', '办事员', 13602939975, 3315505, '', '', '', 40);
INSERT INTO "main"."qingbank_contact" VALUES (339, '', '潘志丽', 'panzhili', 'pzl', '办事员', 13542499155, 3315505, '', '', '', 40);
INSERT INTO "main"."qingbank_contact" VALUES (340, '', '潘顺好', 'panshunhao', 'psh', '办事员', 13750168629, 3315505, '', '', '', 40);
INSERT INTO "main"."qingbank_contact" VALUES (341, '', '梁建梅', 'liangjianmei', 'ljm', '办事员', 13927638333, 3315505, '', '', '', 40);
INSERT INTO "main"."qingbank_contact" VALUES (342, '', '刘伟明', 'liuweiming', 'lwm', '行长', 13927627248, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (343, '', '余丽琴', 'yuliqin', 'ylq', '主管柜员', 13926667217, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (344, '', '邱淑仪', 'qiushuyi', 'qsy', '柜员', 18316013891, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (345, '', '黄银友', 'huangyinyou', 'hyy', '柜员', 15992092087, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (346, '', '姜文峰', 'jiangwenfeng', 'jwf', '柜员', 15807649867, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (347, '', '梁咏华', 'liangyonghua', 'lyh', '柜员', 13413552299, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (348, '', '钟聪俐', 'zhongcongli', 'zcl', '柜员', 15382951424, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (349, '', '胡雪群', 'huxuequn', 'hxq', '柜员', 13178494821, 3925946, '', 3925946, '', 41);
INSERT INTO "main"."qingbank_contact" VALUES (350, '', '袁敏', 'yuanmin', 'ym', '网点负责人', 13501463555, 3924748, '', '', '', 42);
INSERT INTO "main"."qingbank_contact" VALUES (351, '', '黄颖', 'huangying', 'hy', '柜台主管', 13602934626, 3924748, '', '', '', 42);
INSERT INTO "main"."qingbank_contact" VALUES (352, '', '朱丽衡', 'zhuliheng', 'zlh', '办事员', 13727139087, 3924748, '', '', '', 42);
INSERT INTO "main"."qingbank_contact" VALUES (353, '', '罗杏桃', 'luoxingtao', 'lxt', '办事员', 13729614303, 3924748, '', '', '', 42);
INSERT INTO "main"."qingbank_contact" VALUES (354, '', '蔡洁葵', 'caijikui', 'cjk', '办事员', 18926653160, 3924748, '', '', '', 42);
INSERT INTO "main"."qingbank_contact" VALUES (355, '', '林艳明', 'linyanming', 'lym', '行长', 13631088992, 3856365, '', 3856365, '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (356, '', '孔敬', 'kongjing', 'kj', '行长助理', 13922605292, 3856365, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (357, '', '叶翠琼', 'yecuiqiong', 'ycq', '行长助理', 13926667212, 3856365, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (358, '', '苏劲华', 'sujinghua', 'sjh', '信贷负责人', 13828565757, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (359, '', '邓理', 'dengli', 'dl', '客户经理', 18826599116, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (360, '', '彭增', 'pengzeng', 'pz', '客户经理', 13413498850, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (361, '', '骆旋', 'luoxuan', 'lx', '客户经理', 15207647041, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (362, '', '陈海涛', 'chenhaitao', 'cht', '客户经理', 13500295782, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (363, '', '陈琳', 'chenlin', 'cl', '客户经理', 13610592043, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (364, '', '李小花', 'lixiaohua', 'lxh', '信贷资料人', 13926642335, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (365, '', '梁伟平', 'liangweiping', 'lwp', '柜台主管', 13726954182, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (366, '', '练文杰', 'lianwenjie', 'lwj', '报账员', 13922605626, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (367, '', '温淑萍', 'wenshuping', 'wsp', '柜员', 13750113190, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (368, '', '潘彩环', 'pancaihuan', 'pch', '柜员', 13828507506, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (369, '', '李应姗', 'liyingshan', 'lys', '柜员', 15119949813, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (370, '', '邹利影', 'zouliying', 'zly', '柜员', 13172936130, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (371, '', '余璐', 'yulu', 'yl', '柜员', 13726993992, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (372, '', '阮桂环', 'ruanguihuan', 'rgh', '柜员', 15816222818, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (373, '', '黄晓云', 'huangxiaoyun', 'hxy', '柜员', 13927688120, 3859340, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (374, '', '朱国文', 'zhuguowen', 'zgw', '司机', 13602936483, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (375, '', '汤胜蓝', 'tangshenglan', 'tsl', '大堂经理', 13750177404, 3856518, '', '', '', 43);
INSERT INTO "main"."qingbank_contact" VALUES (376, '', '侯展图', 'houzhantu', 'hzt', '行长', 18211320282, 3878005, '', '', '', 44);
INSERT INTO "main"."qingbank_contact" VALUES (377, '', '郑彩凤', 'zhengcaifeng', 'zcf', '柜台主管', 13729670121, 3878005, '', '', '', 44);
INSERT INTO "main"."qingbank_contact" VALUES (378, '', '周劲东', 'zhoujingdong', 'zjd', '柜员', 13926686305, 3878005, '', '', '', 44);
INSERT INTO "main"."qingbank_contact" VALUES (379, '', '潘细珍', 'panxizhen', 'pxz', '柜员', 13927687557, 3878005, '', '', '', 44);
INSERT INTO "main"."qingbank_contact" VALUES (380, '', '邓晓欣', 'dengxiaoxin', 'dxx', '柜员', 18029735968, 3878005, '', '', '', 44);
INSERT INTO "main"."qingbank_contact" VALUES (381, '', '刘杏容', 'liuxingrong', 'lxr', '柜员', 15876320867, 3878005, '', '', '', 44);
INSERT INTO "main"."qingbank_contact" VALUES (382, '', '苏淑浈', 'sushucheng', 'ssc', '大堂经理', 13750115256, 3878005, '', '', '', 44);
INSERT INTO "main"."qingbank_contact" VALUES (383, '', '谢德生', 'xiedesheng', 'xds', '行长', 13828515688, 3360265, '', '', '', 45);
INSERT INTO "main"."qingbank_contact" VALUES (384, '', '廖淑红', 'liaoshuhong', 'lsh', '柜台主管', 13380705985, 3360265, '', '', '', 45);
INSERT INTO "main"."qingbank_contact" VALUES (385, '', '陈旭丽', 'chenxuli', 'cxl', '柜员', 18926690998, 3360265, '', '', '', 45);
INSERT INTO "main"."qingbank_contact" VALUES (386, '', '潘少容', 'panshaorong', 'psr', '柜员', 13828555444, 3360265, '', '', '', 45);
INSERT INTO "main"."qingbank_contact" VALUES (387, '', '张龙', 'zhanglong', 'zl', '柜员', 18316706215, 3360265, '', '', '', 45);
INSERT INTO "main"."qingbank_contact" VALUES (388, '', '刘碧宜', 'liubiyi', 'lby', '柜员', 18926699268, 3360235, '', '', '', 45);
INSERT INTO "main"."qingbank_contact" VALUES (389, '', '黄伟龙', 'huangweilong', 'hwl', '大堂经理', 15119774809, 3360265, '', '', '', 45);
INSERT INTO "main"."qingbank_contact" VALUES (390, '', '许巧文', 'xuqiaowen', 'xqw', '行长', 13076666555, 3362023, '', '', '', 46);
INSERT INTO "main"."qingbank_contact" VALUES (391, '', '麦小云', 'maixiaoyun', 'mxy', '柜台主管', 13927627627, 3362023, '', '', '', 46);
INSERT INTO "main"."qingbank_contact" VALUES (392, '', '李银娇', 'liyinjiao', 'lyj', '柜员', 15014468218, 3362023, '', '', '', 46);
INSERT INTO "main"."qingbank_contact" VALUES (393, '', '黄爱诗', 'huangaishi', 'has', '柜员', 13927665332, 3362023, '', '', '', 46);
INSERT INTO "main"."qingbank_contact" VALUES (394, '', '何静姬', 'hejingji', 'hjj', '柜员', 13705147354, 3362023, '', '', '', 46);
INSERT INTO "main"."qingbank_contact" VALUES (395, '', '黄燕华', 'huangyanhua', 'hyh', '大堂经理', 13726970310, 3362023, '', '', '', 46);
INSERT INTO "main"."qingbank_contact" VALUES (396, '', '曾轶', 'cengyi', 'cy', '分理处负责人', 18023311699, 3360332, '', '', '', 47);
INSERT INTO "main"."qingbank_contact" VALUES (397, '', '何敏华', 'heminhua', 'hmh', '柜台主管', 15915132224, 3360332, '', '', '', 47);
INSERT INTO "main"."qingbank_contact" VALUES (398, '', '欧碧钰', 'oubiyu', 'oby', '柜员', 13679510103, 3360332, '', '', '', 47);
INSERT INTO "main"."qingbank_contact" VALUES (399, '', '叶建英', 'yejianying', 'yjy', '柜员', 13927669118, 3360332, '', '', '', 47);
INSERT INTO "main"."qingbank_contact" VALUES (400, '', '阮锡荣', 'ruanxirong', 'rxr', '柜员', 13620574061, 3360332, '', '', '', 47);
INSERT INTO "main"."qingbank_contact" VALUES (401, '', '曾伟秋', 'cengweiqiu', 'cwq', '大堂经理', 13750107319, 3360332, '', '', '', 47);
INSERT INTO "main"."qingbank_contact" VALUES (402, '', '曾伟秋', 'cengweiqiu', 'cwq', '大堂经理', 13750107319, 3360332, '', '', '', 48);
INSERT INTO "main"."qingbank_contact" VALUES (403, '', '刘健锋', 'liujianfeng', 'ljf', '行长', 13927668828, 3503318, '', '', '', 49);
INSERT INTO "main"."qingbank_contact" VALUES (404, '', '蒙伟', 'mengwei', 'mw', '副行长', 13828568803, 3503308, '', '', '', 49);
INSERT INTO "main"."qingbank_contact" VALUES (405, '', '刘劲', 'liujing', 'lj', '行长助理', 13927686028, 3503299, '', '', '', 49);
INSERT INTO "main"."qingbank_contact" VALUES (406, '', '刘颖桦', 'liuyinghua', 'lyh', '信贷主管', 13926687035, 3502125, '', 3502125, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (407, '', '刘亦中', 'liuyizhong', 'lyz', '客户经理', 13602946811, 3502125, '', 3502126, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (408, '', '夏立强', 'xialiqiang', 'xlq', '客户经理', 13922600261, 3502125, '', 3502127, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (409, '', '谭志权', 'tanzhiquan', 'tzq', '客户经理', 13750104080, 3502125, '', 3502128, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (410, '', '刘景欢', 'liujinghuan', 'ljh', '客户经理', 15019348509, 3502125, '', 3502129, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (411, '', '陈鸣捷', 'chenmingjie', 'cmj', '客户经理', 13500294679, 3502125, '', 3502130, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (412, '', '黄纲艺', 'huanggangyi', 'hgy', '客户经理', 15807647633, 3502125, '', 3502131, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (413, '', '雷颖红', 'leiyinghong', 'lyh', '客户经理', 13828503093, 3502125, '', 3502132, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (414, '', '黄晓艺', 'huangxiaoyi', 'hxy', '客户经理', 13926675566, 3502125, '', 3502133, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (415, '', '黄建辉', 'huangjianhui', 'hjh', '客户经理', 13509261540, 3502125, '', 3502134, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (416, '', '罗喜和', 'luoxihe', 'lxh', '客户经理', 13926669012, 3502125, '', 3502135, '', 50);
INSERT INTO "main"."qingbank_contact" VALUES (417, '', '刘倩稳', 'liuqianwen', 'lqw', '综合柜员', 13924415586, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (418, '', '余丽燕', 'yuliyan', 'yly', '综合柜员', 13380714115, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (419, '', '毛海泉', 'maohaiquan', 'mhq', '综合柜员', 13927653228, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (420, '', '卢波', 'lubo', 'lb', '综合柜员', 18718065100, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (421, '', '廖飞华', 'liaofeihua', 'lfh', '综合柜员', 13926682129, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (422, '', '黄慧', 'huanghui', 'hh', '综合柜员', 13432706555, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (423, '', '杨文', 'yangwen', 'yw', '综合柜员', 13059570722, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (424, '', '杜慧君', 'duhuijun', 'dhj', '报账员', 13413520990, 3502229, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (425, '', '曾美霞', 'cengmeixia', 'cmx', '综合柜员', 13729603491, 3503818, '', '', '', 51);
INSERT INTO "main"."qingbank_contact" VALUES (426, '', '阮丹凤', 'ruandanfeng', 'rdf', '网点负责人', 13750119804, 3378147, '', '', '', 52);
INSERT INTO "main"."qingbank_contact" VALUES (427, '', '梁友银', 'liangyouyin', 'lyy', '综合柜员', 13926685639, 3378147, '', '', '', 52);
INSERT INTO "main"."qingbank_contact" VALUES (428, '', '程记华', 'chengjihua', 'cjh', '综合柜员', 13509260026, 3378147, '', '', '', 52);
INSERT INTO "main"."qingbank_contact" VALUES (429, '', '徐绍民', 'xushaomin', 'xsm', '综合柜员', 13802891029, 3378147, '', '', '', 52);
INSERT INTO "main"."qingbank_contact" VALUES (430, '', '陈朝锐', 'chenzhaorui', 'czr', '综合柜员', 15119773603, 3378147, '', '', '', 52);
INSERT INTO "main"."qingbank_contact" VALUES (431, '', '梁燕媚', 'liangyanmei', 'lym', '网点负责人', 13750101331, 3375559, '', '', '', 53);
INSERT INTO "main"."qingbank_contact" VALUES (432, '', '陈容娣', 'chenrongdi', 'crd', '综合柜员', 13926680796, 3375559, '', '', '', 53);
INSERT INTO "main"."qingbank_contact" VALUES (433, '', '钟有群', 'zhongyouqun', 'zyq', '综合柜员', 13729606478, 3375559, '', '', '', 53);
INSERT INTO "main"."qingbank_contact" VALUES (434, '', '汤炳灿', 'tangbingcan', 'tbc', '综合柜员', 13602938744, 3375559, '', '', '', 53);
INSERT INTO "main"."qingbank_contact" VALUES (435, '', '谢敏', 'xiemin', 'xm', '综合柜员', 13922601079, 3375559, '', '', '', 53);
INSERT INTO "main"."qingbank_contact" VALUES (436, '', '曹鑫', 'caoxin', 'cx', '网点负责人', 13926676464, 3505295, '', '', '', 54);
INSERT INTO "main"."qingbank_contact" VALUES (437, '', '钟海英', 'zhonghaiying', 'zhy', '综合柜员', 13927685383, 3505295, '', '', '', 54);
INSERT INTO "main"."qingbank_contact" VALUES (438, '', '汤利婵', 'tanglichan', 'tlc', '综合柜员', 13417256108, 3505295, '', '', '', 54);
INSERT INTO "main"."qingbank_contact" VALUES (439, '', '刘银顺', 'liuyinshun', 'lys', '综合柜员', 13729637732, 3505295, '', '', '', 54);
INSERT INTO "main"."qingbank_contact" VALUES (440, '', '崔颖', 'cuiying', 'cy', '综合柜员', 15017531763, 3505295, '', '', '', 54);
INSERT INTO "main"."qingbank_contact" VALUES (441, '', '邓丽和', 'denglihe', 'dlh', '网点负责人', 13828557446, 3502280, '', '', '', 55);
INSERT INTO "main"."qingbank_contact" VALUES (442, '', '汤卫庆', 'tangweiqing', 'twq', '综合柜员', 13602934213, 3502280, '', '', '', 55);
INSERT INTO "main"."qingbank_contact" VALUES (443, '', '胡少玲', 'hushaoling', 'hsl', '综合柜员', 13727181323, 3502280, '', '', '', 55);
INSERT INTO "main"."qingbank_contact" VALUES (444, '', '汤焕波', 'tanghuanbo', 'thb', '综合柜员', 13926681282, 3502280, '', '', '', 55);
INSERT INTO "main"."qingbank_contact" VALUES (445, '', '罗慧婷', 'luohuiting', 'lht', '网点负责人', 13828501245, 3502280, '', '', '', 56);
INSERT INTO "main"."qingbank_contact" VALUES (446, '', '陈洁霞', 'chenjixia', 'cjx', '综合柜员', 13922608413, 3375053, '', '', '', 56);
INSERT INTO "main"."qingbank_contact" VALUES (447, '', '阮美容', 'ruanmeirong', 'rmr', '综合柜员', 13824900134, 3367554, '', '', '', 56);
INSERT INTO "main"."qingbank_contact" VALUES (448, '', '雷少文', 'leishaowen', 'lsw', '综合柜员', 13926688309, '', '', '', '', 56);
INSERT INTO "main"."qingbank_contact" VALUES (449, '', '刘建飞', 'liujianfei', 'ljf', '综合柜员', 13610516120, 3332748, '', '', '', 56);
INSERT INTO "main"."qingbank_contact" VALUES (450, '', '胡毅诚', 'huyicheng', 'hyc', '支行行长', 13902353228, 3602752, '', '', '', 57);
INSERT INTO "main"."qingbank_contact" VALUES (451, '', '赖于飞', 'laiyufei', 'lyf', '行长助理', 13828553319, 3602748, '', '', '', 57);
INSERT INTO "main"."qingbank_contact" VALUES (452, '', '唐晓明', 'tangxiaoming', 'txm', '营业部主任', 13631082666, 3601768, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (453, '', '苏秋香', 'suqiuxiang', 'sqx', '柜台主管', 13602921002, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (454, '', '卢碧云', 'lubiyun', 'lby', '账户管理员', 13726956003, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (455, '', '刘燕颜', 'liuyanyan', 'lyy', '报账员', 15816236961, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (456, '', '梁应洪', 'liangyinghong', 'lyh', '综合柜员', 13642524040, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (457, '', '徐振文', 'xuzhenwen', 'xzw', '综合柜员', 13924411130, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (458, '', '潘世林', 'panshilin', 'psl', '综合柜员', 13622936113, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (459, '', '张慧敏', 'zhanghuimin', 'zhm', '综合柜员', 13726967290, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (460, '', '邓蔚', 'dengwei', 'dw', '综合柜员', 13726954836, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (461, '', '吴伟光', 'wuweiguang', 'wwg', '综合柜员', 13726957001, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (462, '', '梁晓彤', 'liangxiaotong', 'lxt', '综合柜员', 15820328180, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (463, '', '张廷敏', 'zhangtingmin', 'ztm', '综合柜员', 13416573910, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (464, '', '罗新明', 'luoxinming', 'lxm', '综合柜员', 13653012866, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (465, '', '陈永权', 'chenyongquan', 'cyq', '大堂经理', 13553925902, 3600057, '', '', '', 58);
INSERT INTO "main"."qingbank_contact" VALUES (466, '', '罗凤腾', 'luofengteng', 'lft', '分理处负责人', 13750110269, 3600366, '', '', '', 59);
INSERT INTO "main"."qingbank_contact" VALUES (467, '', '罗水兴', 'luoshuixing', 'lsx', '柜台主管', 15917626622, 3600366, '', '', '', 59);
INSERT INTO "main"."qingbank_contact" VALUES (468, '', '罗焕玲', 'luohuanling', 'lhl', '综合柜员', 13413511408, 3600366, '', '', '', 59);
INSERT INTO "main"."qingbank_contact" VALUES (469, '', '陈汇', 'chenhui', 'ch', '综合柜员', 13726967492, 3600366, '', '', '', 59);
INSERT INTO "main"."qingbank_contact" VALUES (470, '', '李婉婷', 'liwanting', 'lwt', '大堂经理', 15119928830, 3600366, '', '', '', 59);
INSERT INTO "main"."qingbank_contact" VALUES (471, '', '梁静雯', 'liangjingwen', 'ljw', '大堂经理', 13726981012, 3600366, '', '', '', 59);
INSERT INTO "main"."qingbank_contact" VALUES (472, '', '向嘉隆', 'xiangjialong', 'xjl', '分理处负责人', 13926678864, 3600718, '', '', '', 60);
INSERT INTO "main"."qingbank_contact" VALUES (473, '', '王新群', 'wangxinqun', 'wxq', '柜台主管', 13542495021, 3600718, '', '', '', 60);
INSERT INTO "main"."qingbank_contact" VALUES (474, '', '赖永带', 'laiyongdai', 'lyd', '综合柜员', 13927667901, 3600718, '', '', '', 60);
INSERT INTO "main"."qingbank_contact" VALUES (475, '', '吉伟祥', 'jiweixiang', 'jwx', '综合柜员', 13926663966, 3600718, '', '', '', 60);
INSERT INTO "main"."qingbank_contact" VALUES (476, '', '林桂珍', 'linguizhen', 'lgz', '综合柜员', 13542490700, 3600718, '', '', '', 60);
INSERT INTO "main"."qingbank_contact" VALUES (477, '', '郑志成', 'zhengzhicheng', 'zzc', '分理处负责人', 13927623755, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (478, '', '黄国清', 'huangguoqing', 'hgq', '柜台主管', 13926689677, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (479, '', '邹卫文', 'zouweiwen', 'zww', '综合柜员', 15813232619, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (480, '', '雷国全', 'leiguoquan', 'lgq', '综合柜员', 13535981918, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (481, '', '徐思敏', 'xusimin', 'xsm', '综合柜员', 13924410008, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (482, '', '潘燕君', 'panyanjun', 'pyj', '综合柜员', 13631092659, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (483, '', '潘永强', 'panyongqiang', 'pyq', '综合柜员', 13610567183, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (484, '', '黄细平', 'huangxiping', 'hxp', '大堂经理', 15001647027, 3686405, '', '', '', 61);
INSERT INTO "main"."qingbank_contact" VALUES (485, '', '曾志根', 'cengzhigen', 'czg', '信贷主管', 13927601358, 3605244, '', '', '', 62);
INSERT INTO "main"."qingbank_contact" VALUES (486, '', '陈应波', 'chenyingbo', 'cyb', '客户经理', 13927686681, 3605244, '', '', '', 62);
INSERT INTO "main"."qingbank_contact" VALUES (487, '', '汤国炜', 'tangguowei', 'tgw', '客户经理', 13926612321, 3605244, '', '', '', 62);
INSERT INTO "main"."qingbank_contact" VALUES (488, '', '陈宇航', 'chenyuhang', 'cyh', '客户经理', 13509267067, 3605244, '', '', '', 62);
INSERT INTO "main"."qingbank_contact" VALUES (489, '', '汤健', 'tangjian', 'tj', '客户经理', 13824927779, 3605244, '', '', '', 62);
INSERT INTO "main"."qingbank_contact" VALUES (490, '', '梁秋敏', 'liangqiumin', 'lqm', '客户经理', 18319891914, 3605244, '', '', '', 62);
INSERT INTO "main"."qingbank_contact" VALUES (491, '', '朱雪莹', 'zhuxueying', 'zxy', '信贷资料员', 13926678949, 3605244, '', '', '', 62);
INSERT INTO "main"."qingbank_contact" VALUES (492, '', '温建华', 'wenjianhua', 'wjh', '司机', 18926679432, 3605244, '', '', '', 57);
INSERT INTO "main"."qingbank_contact" VALUES (493, '', '何志强', 'hezhiqiang', 'hzq', '行长', 13828531813, 3608228, '', '', '', 63);
INSERT INTO "main"."qingbank_contact" VALUES (494, '', '刘家辉', 'liujiahui', 'ljh', '副行长', 13927665999, 3608238, '', '', '', 63);
INSERT INTO "main"."qingbank_contact" VALUES (495, '', '卢国田', 'luguotian', 'lgt', '行长助理', 13602946116, 3608318, '', '', '', 63);
INSERT INTO "main"."qingbank_contact" VALUES (496, '', '郑坤', 'zhengkun', 'zk', '信贷主管', 13927661419, 3608368, '', '', '', 64);
INSERT INTO "main"."qingbank_contact" VALUES (497, '', '曾文科', 'cengwenke', 'cwk', '客户经理', 13926611541, 3608368, '', '', '', 64);
INSERT INTO "main"."qingbank_contact" VALUES (498, '', '谭博', 'tanbo', 'tb', '客户经理', 13926683898, 3608368, '', '', '', 64);
INSERT INTO "main"."qingbank_contact" VALUES (499, '', '黄世勇', 'huangshiyong', 'hsy', '信贷资料员', 13926610010, 3608368, '', '', '', 64);
INSERT INTO "main"."qingbank_contact" VALUES (500, '', '李嘉慧', 'lijiahui', 'ljh', '柜员主管', 18029731778, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (501, '', '黄敏虹', 'huangminhong', 'hmh', '会计报帐员', 15219091028, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (502, '', '盘镇鹏', 'panzhenpeng', 'pzp', '对账员', 13542457663, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (503, '', '钟达成', 'zhongdacheng', 'zdc', '柜员', 18948041301, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (504, '', '李建章', 'lijianzhang', 'ljz', '柜员', 13509263408, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (505, '', '赖舒苗', 'laishumiao', 'lsm', '柜员', 15207648707, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (506, '', '曾舒婷', 'cengshuting', 'cst', '柜员', 13750100426, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (507, '', '朱迪思', 'zhudisi', 'zds', '柜员', 15813144161, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (508, '', '封思嘉', 'fengsijia', 'fsj', '大堂经理', 18023723623, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (509, '', '梁秋月', 'liangqiuyue', 'lqy', '饭堂工', 13679518815, 3699826, '', '', '', 65);
INSERT INTO "main"."qingbank_contact" VALUES (510, '', '郭彬洪', 'guobinhong', 'gbh', '网点负责人', 13726989484, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (511, '', '李颖', 'liying', 'ly', '柜员主管', 18998987628, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (512, '', '何沛宁', 'hepeining', 'hpn', '柜员', 18902350661, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (513, '', '陈亮', 'chenliang', 'cl', '柜员', 18926638040, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (514, '', '潘海玲', 'panhailing', 'phl', '柜员', 15807651636, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (515, '', '蓝文生', 'lanwensheng', 'lws', '柜员', 15219083308, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (516, '', '汤道怡', 'tangdaoyi', 'tdy', '柜员', 13726972251, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (517, '', '黄雪银', 'huangxueyin', 'hxy', '大堂经理', 13413505302, 3682386, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (518, '', '马新添', 'maxintian', 'mxt', '保安', 13631063899, 3699826, '', '', '', 66);
INSERT INTO "main"."qingbank_contact" VALUES (519, '', '祝松俊', 'zhusongjun', 'zsj', '网点负责人', 13927607778, 3819016, '', '', '', 67);
INSERT INTO "main"."qingbank_contact" VALUES (520, '', '杜炳章', 'dubingzhang', 'dbz', '柜员主管', 13927626680, 3819016, '', '', '', 67);
INSERT INTO "main"."qingbank_contact" VALUES (521, '', '林敏华', 'linminhua', 'lmh', '柜员', 18948048428, 3819016, '', '', '', 67);
INSERT INTO "main"."qingbank_contact" VALUES (522, '', '邹施莹', 'zoushiying', 'zsy', '柜员', 18029768572, 3819016, '', '', '', 67);
INSERT INTO "main"."qingbank_contact" VALUES (523, '', '胡意珞', 'huyiluo', 'hyl', '柜员', 15219077259, 3819016, '', '', '', 67);
INSERT INTO "main"."qingbank_contact" VALUES (524, '', '郑国昌', 'zhengguochang', 'zgc', '柜员', 13415208010, 3819016, '', '', '', 67);
INSERT INTO "main"."qingbank_contact" VALUES (525, '', '黄玉娣', 'huangyudi', 'hyd', '饭堂工', 15914979880, 3819016, '', '', '', 67);
INSERT INTO "main"."qingbank_contact" VALUES (526, '', '吴细成', 'wuxicheng', 'wxc', '支行行长', 13602945431, 3244138, '', 3244349, '', 68);
INSERT INTO "main"."qingbank_contact" VALUES (527, '', '张广财', 'zhangguangcai', 'zgc', '支行副行长', 13631083208, 3244992, '', 3244349, '', 68);
INSERT INTO "main"."qingbank_contact" VALUES (528, '', '林焕斌', 'linhuanbin', 'lhb', '营业部主任', 13727116181, 3244198, '', 3244349, '', 68);
INSERT INTO "main"."qingbank_contact" VALUES (529, '', '黄桂忠', 'huangguizhong', 'hgz', '司机', 13509260321, 3244349, '', 3244349, '', 68);
INSERT INTO "main"."qingbank_contact" VALUES (530, '', '黄翠红', 'huangcuihong', 'hch', '信贷资料员', 15089742398, 3244349, '', 3244349, '', 69);
INSERT INTO "main"."qingbank_contact" VALUES (531, '', '卢焕均', 'luhuanjun', 'lhj', '客户经理', 13927668763, 3244349, '', 3244349, '', 69);
INSERT INTO "main"."qingbank_contact" VALUES (532, '', '卢记林', 'lujilin', 'ljl', '客户经理', 13500298751, 3244349, '', 3244349, '', 69);
INSERT INTO "main"."qingbank_contact" VALUES (533, '', '陈晓冠', 'chenxiaoguan', 'cxg', '客户经理', 18900893947, 3244349, '', 3244349, '', 69);
INSERT INTO "main"."qingbank_contact" VALUES (534, '', '周俊', 'zhoujun', 'zj', '信贷主管', 13726996282, 3244349, '', 3244349, '', 69);
INSERT INTO "main"."qingbank_contact" VALUES (535, '', '邱洁英', 'qiujiying', 'qjy', '报账员', 13417283998, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (536, '', '李水连', 'lishuilian', 'lsl', '柜员', 13610523779, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (537, '', '罗镜钊', 'luojingzhao', 'ljz', '柜员', 15089743058, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (538, '', '陈金爱', 'chenjinai', 'cja', '柜员', 13413469323, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (539, '', '罗锦钊', 'luojinzhao', 'ljz', '柜员', 13610514400, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (540, '', '杨爱清', 'yangaiqing', 'yaq', '柜员', 13413532599, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (541, '', '覃玉文', 'tanyuwen', 'tyw', '柜员', 13415205277, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (542, '', '钟艳华', 'zhongyanhua', 'zyh', '柜员', 15813253434, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (543, '', '潘华森', 'panhuasen', 'phs', '柜员', 13602947501, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (544, '', '杨洁行', 'yangjixing', 'yjx', '柜员', 15816299910, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (545, '', '叶上勇', 'yeshangyong', 'ysy', '柜员', 13679521907, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (546, '', '李艺', 'liyi', 'ly', '柜员', 13535970891, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (547, '', '余大鹏', 'yudapeng', 'ydp', '柜员', 13413527383, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (548, '', '邝伟杰', 'kuangweijie', 'kwj', '柜员', 13413583210, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (549, '', '邓研科', 'dengyanke', 'dyk', '柜员', 18344008317, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (550, '', '龙凤茹', 'longfengru', 'lfr', '柜员', 13828500763, 3243374, '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (551, '', '陈敬联', 'chenjinglian', 'cjl', '柜员', 13553903198, 3243385, '', '', '', 71);
INSERT INTO "main"."qingbank_contact" VALUES (552, '', '邓笑欢', 'dengxiaohuan', 'dxh', '网点负责人', 13828508546, 3243385, '', '', '', 71);
INSERT INTO "main"."qingbank_contact" VALUES (553, '', '潘文英', 'panwenying', 'pwy', '柜员', 13727198193, 3243385, '', '', '', 71);
INSERT INTO "main"."qingbank_contact" VALUES (554, '', '禤瑞娜', 'xuanruinuo', 'xrn', '柜员', 15017515173, 3243385, '', '', '', 71);
INSERT INTO "main"."qingbank_contact" VALUES (555, '', '潘树强', 'panshuqiang', 'psq', '柜员', 13376667558, 3243295, '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (556, '', '郑晓丽', 'zhengxiaoli', 'zxl', '网点负责人', 15820337922, 3243295, '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (557, '', '蔡茗芬', 'caimingfen', 'cmf', '柜员', 13413505333, 3243295, '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (558, '', '潘耀棠', 'panyaotang', 'pyt', '柜员', 13680011218, 3243295, '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (559, '', '张榕荣', 'zhangrongrong', 'zrr', '柜员', 13553962721, 3243295, '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (560, '', '李炽强', 'lichiqiang', 'lcq', '柜员', 13727133882, 3243295, '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (561, '', '曹丽金', 'caolijin', 'clj', '柜员', 13417202828, 3243295, '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (562, '', '徐炳坤', 'xubingkun', 'xbk', '柜员', 13927667543, 3293057, '', '', '', 73);
INSERT INTO "main"."qingbank_contact" VALUES (563, '', '郭咏安', 'guoyongan', 'gya', '网点负责人', 13553996774, 3293057, '', '', '', 73);
INSERT INTO "main"."qingbank_contact" VALUES (564, '', '冯伟杰', 'fengweijie', 'fwj', '柜员', 13509269299, 3293057, '', '', '', 73);
INSERT INTO "main"."qingbank_contact" VALUES (565, '', '温志杰', 'wenzhijie', 'wzj', '柜员', 13542470122, 3293057, '', '', '', 73);
INSERT INTO "main"."qingbank_contact" VALUES (566, '', '颜杰', 'yanjie', 'yj', '柜员', 13610538969, 3293057, '', '', '', 73);
INSERT INTO "main"."qingbank_contact" VALUES (567, '', '邱柏灵', 'qiubailing', 'qbl', '柜员', 13602945202, 3293057, '', '', '', 73);
INSERT INTO "main"."qingbank_contact" VALUES (568, '', '陈颖', 'chenying', 'cy', '大堂经理', 13535470355, '', '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (569, '', '姜国君', 'jiangguojun', 'jgj', '大堂经理', 15975889112, '', '', '', '', 70);
INSERT INTO "main"."qingbank_contact" VALUES (570, '', '黄焕桃', 'huanghuantao', 'hht', '大堂经理', 13432707123, '', '', '', '', 72);
INSERT INTO "main"."qingbank_contact" VALUES (571, '', '刘柏灵', 'liubailing', 'lbl', '大堂经理', 13926662086, '', '', '', '', 71);
INSERT INTO "main"."qingbank_contact" VALUES (572, '', '陈海云', 'chenhaiyun', 'chy', '行长', 13509266478, 3207109, '', 3201341, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (573, '', '郭尚恩', 'guoshangen', 'gse', '副行长', 13824911800, 3203244, '', 3201341, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (574, '', '叶钻虹', 'yezuanhong', 'yzh', '行长助理', 13926647480, 3206366, '', 3201341, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (575, '', '林永兴', 'linyongxing', 'lyx', '客户经理', 13509260377, 3201341, '', 3201341, '', 75);
INSERT INTO "main"."qingbank_contact" VALUES (576, '', '刘永成', 'liuyongcheng', 'lyc', '客户经理', 13922608138, 3201341, '', 3201341, '', 75);
INSERT INTO "main"."qingbank_contact" VALUES (577, '', '覃伟健', 'tanweijian', 'twj', '客户经理', 13500297890, 3201341, '', 3201341, '', 75);
INSERT INTO "main"."qingbank_contact" VALUES (578, '', '林浩均', 'linhaojun', 'lhj', '客户经理', 18926679912, 3201341, '', 3201341, '', 75);
INSERT INTO "main"."qingbank_contact" VALUES (579, '', '王肖', 'wangxiao', 'wx', '客户经理', 13926685445, 3201341, '', 3201341, '', 75);
INSERT INTO "main"."qingbank_contact" VALUES (580, '', '潘嘉明', 'panjiaming', 'pjm', '资料员', 13926688855, 3201341, '', 3201341, '', 75);
INSERT INTO "main"."qingbank_contact" VALUES (581, '', '李民文', 'liminwen', 'lmw', '司机', 13509263912, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (582, '', '朱思敏', 'zhusimin', 'zsm', '报账员', 15813230169, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (583, '', '莫格力', 'mogeli', 'mgl', '柜员', 13922602326, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (584, '', '林显聪', 'linxiancong', 'lxc', '柜员', 15807647656, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (585, '', '刘计兴', 'liujixing', 'ljx', '柜员', 13425210108, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (586, '', '蒋学智', 'jiangxuezhi', 'jxz', '柜员', 15807649654, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (587, '', '何欣', 'hexin', 'hx', '柜员', 15119789735, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (588, '', '朱依敏', 'zhuyimin', 'zym', '柜员', 15813263884, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (589, '', '冯丽华', 'fenglihua', 'flh', '柜员', 13415289140, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (590, '', '向燕娜', 'xiangyannuo', 'xyn', '柜员', 13413523044, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (591, '', '王静', 'wangjing', 'wj', '柜员', 15602356461, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (592, '', '谭春玲', 'tanchunling', 'tcl', '柜员', 15992011740, 3201473, '', 3201340, '', 74);
INSERT INTO "main"."qingbank_contact" VALUES (593, '', '何永亮', 'heyongliang', 'hyl', '经理助理', 13824929747, 3207212, '', '', '', 76);
INSERT INTO "main"."qingbank_contact" VALUES (594, '', '冯细清', 'fengxiqing', 'fxq', '柜员', 13602945145, 3207212, '', '', '', 76);
INSERT INTO "main"."qingbank_contact" VALUES (595, '', '侯佩施', 'houpeishi', 'hps', '柜员', 13726958063, 3207212, '', '', '', 76);
INSERT INTO "main"."qingbank_contact" VALUES (596, '', '朱宁欣', 'zhuningxin', 'znx', '柜员', 15913165166, 3207212, '', '', '', 76);
INSERT INTO "main"."qingbank_contact" VALUES (597, '', '巩星照', 'gongxingzhao', 'gxz', '经理助理', 13432701952, 3202639, '', '', '', 77);
INSERT INTO "main"."qingbank_contact" VALUES (598, '', '陈燕华', 'chenyanhua', 'cyh', '柜员', 13802894664, 3202639, '', '', '', 77);
INSERT INTO "main"."qingbank_contact" VALUES (599, '', '姚科万', 'yaokewan', 'ykw', '柜员', 13926670704, 3202639, '', '', '', 77);
INSERT INTO "main"."qingbank_contact" VALUES (600, '', '冯玉珍', 'fengyuzhen', 'fyz', '柜员', 13413561266, 3202639, '', '', '', 77);
INSERT INTO "main"."qingbank_contact" VALUES (601, '', '袁正锋', 'yuanzhengfeng', 'yzf', '经理助理', 13726966389, 3723441, '', '', '', 78);
INSERT INTO "main"."qingbank_contact" VALUES (602, '', '罗有洪', 'luoyouhong', 'lyh', '柜员', 13610527083, 3723441, '', '', '', 78);
INSERT INTO "main"."qingbank_contact" VALUES (603, '', '罗文飞', 'luowenfei', 'lwf', '柜员', 13927661600, 3723441, '', '', '', 78);
INSERT INTO "main"."qingbank_contact" VALUES (604, '', '龙小恒', 'longxiaoheng', 'lxh', '柜员', 13750141234, 3723441, '', '', '', 78);
INSERT INTO "main"."qingbank_contact" VALUES (605, '', '黄浩荣', 'huanghaorong', 'hhr', '柜员', 13926640433, 3723441, '', '', '', 78);
INSERT INTO "main"."qingbank_contact" VALUES (606, '', '李梅娟', 'limeijuan', 'lmj', '柜员', 15102029950, 3723441, '', '', '', 78);
INSERT INTO "main"."qingbank_contact" VALUES (607, '', '黄锐文', 'huangruiwen', 'hrw', '柜员', 13326548116, 3723441, '', '', '', 78);
INSERT INTO "main"."qingbank_contact" VALUES (608, '', '钟伟明', 'zhongweiming', 'zwm', '经理助理', 13602933172, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (609, '', '钟树辉', 'zhongshuhui', 'zsh', '柜员', 13926684532, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (610, '', '黄志洪', 'huangzhihong', 'hzh', '柜员', 13501469482, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (611, '', '谢学斌', 'xiexuebin', 'xxb', '柜员', 13927689256, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (612, '', '杨俊涛', 'yangjuntao', 'yjt', '柜员', 13922602717, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (613, '', '明素梅', 'mingsumei', 'msm', '柜员', 15014225065, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (614, '', '刘恩韶', 'liuenshao', 'les', '柜员', 13726990097, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (615, '', '欧向勇', 'ouxiangyong', 'oxy', '柜员', 18702057571, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (616, '', '郭翠玲', 'guocuiling', 'gcl', '柜员', 15915199711, 3730972, '', '', '', 79);
INSERT INTO "main"."qingbank_contact" VALUES (617, '', '冯文杰', 'fengwenjie', 'fwj', '经理助理', 15807658781, 3729324, '', '', '', 80);
INSERT INTO "main"."qingbank_contact" VALUES (618, '', '吴子健', 'wuzijian', 'wzj', '柜员', 13425204710, 3729324, '', '', '', 80);
INSERT INTO "main"."qingbank_contact" VALUES (619, '', '罗渭志', 'luoweizhi', 'lwz', '柜员', 13242392097, 3729324, '', '', '', 80);
INSERT INTO "main"."qingbank_contact" VALUES (620, '', '曾耀辉', 'cengyaohui', 'cyh', '柜员', 13602944882, 3729324, '', '', '', 80);
INSERT INTO "main"."qingbank_contact" VALUES (621, '', '梁兴华', 'liangxinghua', 'lxh', '行长', 13926686620, 3662102, '', '', '', 81);
INSERT INTO "main"."qingbank_contact" VALUES (622, '', '文武健', 'wenwujian', 'wwj', '副行长', 13922608066, 3662106, '', '', '', 81);
INSERT INTO "main"."qingbank_contact" VALUES (623, '', '王结云', 'wangjieyun', 'wjy', '行长助理', 13926673012, 3662103, '', '', '', 81);
INSERT INTO "main"."qingbank_contact" VALUES (624, '', '潘润锋', 'panrunfeng', 'prf', '信贷主管', 13922602765, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (625, '', '潘少洪', 'panshaohong', 'psh', '客户经理', 13626610603, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (626, '', '廖小聪', 'liaoxiaocong', 'lxc', '客户经理', 13927683014, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (627, '', '陈浩', 'chenhao', 'ch', '客户经理', 13610555774, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (628, '', '张家杰', 'zhangjiajie', 'zjj', '客户经理', 13828551157, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (629, '', '陈瑞光', 'chenruiguang', 'crg', '客户经理', 13602942500, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (630, '', '林浩新', 'linhaoxin', 'lhx', '客户经理', 138028901240, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (631, '', '李一滨', 'liyibin', 'lyb', '信贷资料员', 13726999598, 3662105, '', 3662105, '', 82);
INSERT INTO "main"."qingbank_contact" VALUES (632, '', '汤再兴', 'tangzaixing', 'tzx', '柜台主管', 13828508490, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (633, '', '李佩玲', 'lipeiling', 'lpl', '办事员', 18926673456, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (634, '', '郭卫强', 'guoweiqiang', 'gwq', '办事员', 13318610670, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (635, '', '潘艳娜', 'panyannuo', 'pyn', '办事员', 15089727002, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (636, '', '刘咏茹', 'liuyongru', 'lyr', '办事员', 15917635317, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (637, '', '徐俏艳', 'xuqiaoyan', 'xqy', '办事员', 15820324522, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (638, '', '蔡洁莹', 'caijiying', 'cjy', '办事员', 13413533219, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (639, '', '黄燕玲', 'huangyanling', 'hyl', '办事员', 18666926986, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (640, '', '巫娴', 'wuxian', 'wx', '办事员', 18666692490, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (641, '', '张彦霞', 'zhangyanxia', 'zyx', '办事员', 18926681887, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (642, '', '张健', 'zhangjian', 'zj', '办事员', 13413512897, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (643, '', '罗燕姬', 'luoyanji', 'lyj', '大堂经理', 13750110292, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (644, '', '郑力争', 'zhenglizheng', 'zlz', '保安', 13680010887, '3379444/3367083', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (645, '', '刘雪梅', 'liuxuemei', 'lxm', '炊事员', 13416582626, '3379444/3367084', '', '', '', 83);
INSERT INTO "main"."qingbank_contact" VALUES (646, '', '郭尹平', 'guoyinping', 'gyp', '经理助理', 13824926348, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (647, '', '蔡永光', 'caiyongguang', 'cyg', '柜台主管', 13926683033, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (648, '', '钟桂新', 'zhongguixin', 'zgx', '办事员', 13509269439, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (649, '', '冼文婷', 'xianwenting', 'xwt', '办事员', 13415285766, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (650, '', '张素文', 'zhangsuwen', 'zsw', '办事员', 15915182348, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (651, '', '欧金燕', 'oujinyan', 'ojy', '办事员', 13727150957, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (652, '', '黄凝慧', 'huangninghui', 'hnh', '办事员', 13750171835, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (653, '', '黄  胜', 'huang  sheng', 'h  s', '大堂经理', 18666696265, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (654, '', '余丽敏', 'yulimin', 'ylm', '大堂经理', 13416533141, 3550263, '', '', '', 84);
INSERT INTO "main"."qingbank_contact" VALUES (655, '', '陈细棠', 'chenxitang', 'cxt', '经理助理', 13500298286, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (656, '', '刘俊锋', 'liujunfeng', 'ljf', '柜台主管', 13926668616, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (657, '', '向悦强', 'xiangyueqiang', 'xyq', '办事员', 13076613106, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (658, '', '刘少珍', 'liushaozhen', 'lsz', '办事员', 13553920331, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (659, '', '罗锦颜', 'luojinyan', 'ljy', '办事员', 18926651322, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (660, '', '陶鑫湾', 'taoxinwan', 'txw', '办事员', 13922561322, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (661, '', '潘玲燕', 'panlingyan', 'ply', '大堂经理', 13413582820, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (662, '', '龙观水', 'longguanshui', 'lgs', '保安', 13178463618, 3483261, '', '', '', 85);
INSERT INTO "main"."qingbank_contact" VALUES (663, '', '刘 炽', 'liu chi', 'l c', '经理助理', 13726994104, 3555163, '', '', '', 86);
INSERT INTO "main"."qingbank_contact" VALUES (664, '', '潘伟锋', 'panweifeng', 'pwf', '柜台主管', 13922609300, 3555163, '', '', '', 86);
INSERT INTO "main"."qingbank_contact" VALUES (665, '', '廖 鹏', 'liao peng', 'l p', '办事员', 13413533654, 3555163, '', '', '', 86);
INSERT INTO "main"."qingbank_contact" VALUES (666, '', '郭志英', 'guozhiying', 'gzy', '办事员', 13431960768, 3555163, '', '', '', 86);
INSERT INTO "main"."qingbank_contact" VALUES (667, '', '李建环', 'lijianhuan', 'ljh', '办事员', 13539525573, 3555163, '', '', '', 86);
INSERT INTO "main"."qingbank_contact" VALUES (668, '', '朱志飞', 'zhuzhifei', 'zzf', '保安', 13620588986, 3555163, '', '', '', 86);
INSERT INTO "main"."qingbank_contact" VALUES (669, '', '曹文坚', 'caowenjian', 'cwj', '支行行长', 13828552586, 3840338, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (670, '', '朱力方', 'zhulifang', 'zlf', '支行副行长', 13602939692, 3840339, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (671, '', '郭丽敏', 'guolimin', 'glm', '营业部主任', 13926689845, 3840340, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (672, '', '邓哲勇', 'dengzheyong', 'dzy', '信贷主管', 13926673006, 3840701, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (673, '', '曾细兴', 'cengxixing', 'cxx', '客户经理', 13602946781, 3840701, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (674, '', '钟建军', 'zhongjianjun', 'zjj', '客户经理', 13926671788, 3840701, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (675, '', '杨文芳', 'yangwenfang', 'ywf', '客户经理', 13602931985, 3840701, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (676, '', '黄其星', 'huangqixing', 'hqx', '信贷资料员', 13926614483, 3840701, '', 3840721, '', 87);
INSERT INTO "main"."qingbank_contact" VALUES (677, '', '罗西荣', 'luoxirong', 'lxr', '高级柜员', 13828554911, 3840721, '', 3840721, '', 88);
INSERT INTO "main"."qingbank_contact" VALUES (678, '', '翁炽辉', 'wengchihui', 'wch', '综合柜员', 13509252921, 3840721, '', 3840721, '', 88);
INSERT INTO "main"."qingbank_contact" VALUES (679, '', '陈丽华', 'chenlihua', 'clh', '综合柜员', 13750189211, 3840721, '', 3840721, '', 88);
INSERT INTO "main"."qingbank_contact" VALUES (680, '', '张琪', 'zhangqi', 'zq', '综合柜员', 13631098152, 3840721, '', 3840721, '', 88);
INSERT INTO "main"."qingbank_contact" VALUES (681, '', '陈桂秋', 'chenguiqiu', 'cgq', '综合柜员', 13727167718, 3840721, '', 3840721, '', 88);
INSERT INTO "main"."qingbank_contact" VALUES (682, '', '罗肖理', 'luoxiaoli', 'lxl', '综合柜员', 13763321636, 3840721, '', 3840721, '', 88);
INSERT INTO "main"."qingbank_contact" VALUES (683, '', '黄哲', 'huangzhe', 'hz', '综合柜员', 13750100166, 3840721, '', 3840721, '', 88);
INSERT INTO "main"."qingbank_contact" VALUES (684, '', '杨佩云', 'yangpeiyun', 'ypy', '网点负责人', 13924429990, 3210325, '', '', '', 89);
INSERT INTO "main"."qingbank_contact" VALUES (685, '', '黄镜清', 'huangjingqing', 'hjq', '高级柜员', 13802898100, 3210325, '', '', '', 89);
INSERT INTO "main"."qingbank_contact" VALUES (686, '', '梁志坚', 'liangzhijian', 'lzj', '综合柜员', 13602931422, 3210325, '', '', '', 89);
INSERT INTO "main"."qingbank_contact" VALUES (687, '', '李进宇', 'lijinyu', 'ljy', '综合柜员', 13927631115, 3210325, '', '', '', 89);
INSERT INTO "main"."qingbank_contact" VALUES (688, '', '张桂新', 'zhangguixin', 'zgx', '综合柜员', 13501461155, 3210325, '', '', '', 89);
INSERT INTO "main"."qingbank_contact" VALUES (689, '', '易佳丽', 'yijiali', 'yjl', '综合柜员', 13620570155, 3210325, '', '', '', 89);
INSERT INTO "main"."qingbank_contact" VALUES (690, '', '黄玉君', 'huangyujun', 'hyj', '综合柜员', 18666693892, 3210325, '', '', '', 89);
INSERT INTO "main"."qingbank_contact" VALUES (691, '', '刘锐基', 'liuruiji', 'lrj', '网点负责人', 13828558531, 3215026, '', '', '', 90);
INSERT INTO "main"."qingbank_contact" VALUES (692, '', '陆丈庭', 'luzhangting', 'lzt', '高级柜员', 13602939762, 3215026, '', '', '', 90);
INSERT INTO "main"."qingbank_contact" VALUES (693, '', '罗金清', 'luojinqing', 'ljq', '综合柜员', 13828553245, 3215026, '', '', '', 90);
INSERT INTO "main"."qingbank_contact" VALUES (694, '', '张卫洪', 'zhangweihong', 'zwh', '综合柜员', 13602948627, 3215026, '', '', '', 90);
INSERT INTO "main"."qingbank_contact" VALUES (695, '', '夏永科', 'xiayongke', 'xyk', '综合柜员', 13926682056, 3215026, '', '', '', 90);
INSERT INTO "main"."qingbank_contact" VALUES (696, '', '白丽华', 'bailihua', 'blh', '综合柜员', 13927669802, 3215026, '', '', '', 90);

-- ----------------------------
-- Table structure for qingbank_department
-- ----------------------------
DROP TABLE IF EXISTS "main"."qingbank_department";
CREATE TABLE qingbank_department (
	id INTEGER NOT NULL, 
	name VARCHAR(20), 
	address VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);

-- ----------------------------
-- Records of qingbank_department
-- ----------------------------
INSERT INTO "main"."qingbank_department" VALUES (1, '领导班子', null);
INSERT INTO "main"."qingbank_department" VALUES (2, '办公室', null);
INSERT INTO "main"."qingbank_department" VALUES (3, '行政服务中心', null);
INSERT INTO "main"."qingbank_department" VALUES (4, '科技部', null);
INSERT INTO "main"."qingbank_department" VALUES (5, '人力资源部', null);
INSERT INTO "main"."qingbank_department" VALUES (6, '计划财务部', null);
INSERT INTO "main"."qingbank_department" VALUES (7, '金融市场部', null);
INSERT INTO "main"."qingbank_department" VALUES (8, '会计结算部', null);
INSERT INTO "main"."qingbank_department" VALUES (9, '会计结算部事后监督中心', null);
INSERT INTO "main"."qingbank_department" VALUES (10, '会计结算部清算中心', null);
INSERT INTO "main"."qingbank_department" VALUES (11, '安全保卫部', null);
INSERT INTO "main"."qingbank_department" VALUES (12, '内审稽核部', null);
INSERT INTO "main"."qingbank_department" VALUES (13, '合规与风险管理部', null);
INSERT INTO "main"."qingbank_department" VALUES (14, '资产保全部', null);
INSERT INTO "main"."qingbank_department" VALUES (15, '授信管理部', null);
INSERT INTO "main"."qingbank_department" VALUES (16, '小企业专营中心', null);
INSERT INTO "main"."qingbank_department" VALUES (17, '公司银行部', null);
INSERT INTO "main"."qingbank_department" VALUES (18, '机构银行部', null);
INSERT INTO "main"."qingbank_department" VALUES (19, '零售银行部', null);
INSERT INTO "main"."qingbank_department" VALUES (20, '营业部副总经理室', null);
INSERT INTO "main"."qingbank_department" VALUES (21, '营业部客户经理室', null);
INSERT INTO "main"."qingbank_department" VALUES (22, '营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (23, '凤城支行', null);
INSERT INTO "main"."qingbank_department" VALUES (24, '凤城支行信贷室', null);
INSERT INTO "main"."qingbank_department" VALUES (25, '凤城支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (26, '凤城支行凤苑分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (27, '凤城支行古城分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (28, '凤城支行湖滨分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (29, '凤城支行清郊分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (30, '凤城支行松鹤分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (31, '凤城支行西湖分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (32, '东城支行行长室', null);
INSERT INTO "main"."qingbank_department" VALUES (33, '东城支行副行长室', null);
INSERT INTO "main"."qingbank_department" VALUES (34, '东城支行办公室', null);
INSERT INTO "main"."qingbank_department" VALUES (35, '东城支行信贷室', null);
INSERT INTO "main"."qingbank_department" VALUES (36, '东城支行按揭中心', null);
INSERT INTO "main"."qingbank_department" VALUES (37, '东城东郊支行', null);
INSERT INTO "main"."qingbank_department" VALUES (38, '东城支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (39, '东城支行跃进分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (40, '东城支行桥北分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (41, '东城兰水支行', null);
INSERT INTO "main"."qingbank_department" VALUES (42, '东城支行阳光分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (43, '小市支行', null);
INSERT INTO "main"."qingbank_department" VALUES (44, '小市三角支行', null);
INSERT INTO "main"."qingbank_department" VALUES (45, '小市江南分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (46, '小市恒福支行', null);
INSERT INTO "main"."qingbank_department" VALUES (47, '小市新城分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (48, '小市新城支行', null);
INSERT INTO "main"."qingbank_department" VALUES (49, '洲心支行', null);
INSERT INTO "main"."qingbank_department" VALUES (50, '洲心支行信贷室', null);
INSERT INTO "main"."qingbank_department" VALUES (51, '洲心支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (52, '洲心支行凤凰分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (53, '洲心支行连石分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (54, '洲心支行龙华分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (55, '洲心支行清源分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (56, '洲心支行银泉分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (57, '龙塘支行', null);
INSERT INTO "main"."qingbank_department" VALUES (58, '龙塘支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (59, '龙塘支行城南分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (60, '龙塘支行新庄分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (61, '龙塘支行沙溪分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (62, '龙塘支行信贷室', null);
INSERT INTO "main"."qingbank_department" VALUES (63, '银盏支行', null);
INSERT INTO "main"."qingbank_department" VALUES (64, '银盏支行信贷室', null);
INSERT INTO "main"."qingbank_department" VALUES (65, '银盏支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (66, '银盏支行泰基分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (67, '银盏支行嘉福分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (68, '源潭支行', null);
INSERT INTO "main"."qingbank_department" VALUES (69, '源潭支行信贷部', null);
INSERT INTO "main"."qingbank_department" VALUES (70, '源潭支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (71, '源潭支行新星分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (72, '源潭支行大连分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (73, '源潭支行高桥分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (74, '石角支行', null);
INSERT INTO "main"."qingbank_department" VALUES (75, '石角支行信贷室', null);
INSERT INTO "main"."qingbank_department" VALUES (76, '石角支行塘头分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (77, '石角支行城中分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (78, '石角支行塘基分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (79, '石角兴仁支行', null);
INSERT INTO "main"."qingbank_department" VALUES (80, '石角支行界牌分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (81, '横荷支行', null);
INSERT INTO "main"."qingbank_department" VALUES (82, '横荷支行信贷室', null);
INSERT INTO "main"."qingbank_department" VALUES (83, '横荷支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (84, '横荷支行百加分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (85, '横荷支行佛祖分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (86, '横荷支行荷塘分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (87, '飞来峡支行', null);
INSERT INTO "main"."qingbank_department" VALUES (88, '飞来峡支行营业部', null);
INSERT INTO "main"."qingbank_department" VALUES (89, '飞来峡支行江口分理处', null);
INSERT INTO "main"."qingbank_department" VALUES (90, '飞来峡支行高田分理处', null);

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS "main"."role";
CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	description VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO "main"."role" VALUES (1, 'admin', '管理员');
INSERT INTO "main"."role" VALUES (2, '员工', '');

-- ----------------------------
-- Table structure for roles_users
-- ----------------------------
DROP TABLE IF EXISTS "main"."roles_users";
CREATE TABLE roles_users (
	user_id INTEGER, 
	role_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);

-- ----------------------------
-- Records of roles_users
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "main"."user";
CREATE TABLE user (
	id INTEGER NOT NULL, 
	email VARCHAR(255), 
	password VARCHAR(255), 
	active BOOLEAN, 
	last_login_at DATETIME, 
	current_login_at DATETIME, 
	last_login_ip VARCHAR(80), 
	current_login_ip VARCHAR(80), 
	login_count INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	CHECK (active IN (0, 1))
);

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "main"."user" VALUES (1, 'kinorsi@gmail.com', '520luyasi', 1, '2013-12-26 03:35:14.357000', '2013-12-26 09:41:49.444000', '127.0.0.1', '127.0.0.1', 3);
