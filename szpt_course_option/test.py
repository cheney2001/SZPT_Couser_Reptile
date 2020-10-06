from szpt_course_option.courseOption import CourseOptions
from lxml import etree
import collections
import json

tree = lambda: collections.defaultdict(tree)

html_text = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>

<HEAD>
    <title>任选课课表</title>
    <link href="Style/iestyle.css" type="text/css" rel="stylesheet">
    <meta content="Microsoft Visual Studio .NET 7.1" name="GENERATOR">
    <meta content="C#" name="CODE_LANGUAGE">
    <meta content="JavaScript" name="vs_defaultClientScript">
    <meta content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema">
</HEAD>
<script language="Javascript">
    function redirectHttpToHttps() {
        var url = window.location.href;
        if (url.indexOf("https") < 0) {
            url = url.replace("http:", "https:");
            window.location.replace(url);
        }
    }
    redirectHttpToHttps();
</script>

<body ms_positioning="FlowLayout">
    <table border="0" width="100%">
        <tr>
            <td colspan="2" width="100%">
                <table id="_ctl1_pnlHeaderGlobal" class="HeaderFriends" cellpadding="0" cellspacing="0" border="0"
                    width="100%">
                    <tr>
                        <td>
                            深职院综合教务系统
                            <img id="_ctl1_imgFriends" class="HeaderImage" src="Images/logo.gif" alt="" border="0"
                                height="35" />
                        </td>
                    </tr>
                </table>
                <table id="_ctl1_pnlHeaderLocal" class="HeaderTitle" cellpadding="0" cellspacing="0" border="0"
                    width="100%">
                    <tr>
                        <td>

                            <img id="_ctl1_imgIcon" class="HeaderImage" src="Images/homeconnected.gif" alt=""
                                border="0" />
                            <span id="_ctl1_lblWelcome">欢迎访问！</span>

                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td colspan="2" width="100%"><span class="SubHeader"><a
                        href="http://jiaowc.szpt.edu.cn/newjw/index.asp">教务处</a><span>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</span><a
                        href="http://dudao.szpt.edu.cn/">督导室</a><span>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</span><a
                        href="http://www.lib.szpt.edu.cn/">图书馆</a><span>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</span><a
                        href="/SzptJwBsII/default.aspx">功能列表</a><span>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</span><a
                        href="/SzptJwBsII/Secure/login.aspx">重新登录</a><span>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp2020年10月3日</span></span>
            </td>
        </tr>
        <tr>
            <td width="5%">
                <p>
                    <font face="宋体"></font>
                    <font face="宋体">
                        <table id="_ctl3_Panel1" cellpadding="0" cellspacing="0" border="0" height="300" width="122">
                            <tr>
                                <td>

                                    <P>&nbsp;</P>
                                    <P>
                                    <div class="treeview" id="_ctl3_TreeView_stdnt" class="treeview"
                                        style="height:420px;width:134px;height:420px;width:134px;">
                                        <table CELLSPACING="0" CELLPADDING="0" BORDER="0">
                                            <TR>
                                                <TD valign='middle'>&nbsp;<a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','oncollapse,0')"><IMG
                                                            align='top' border='0' class='icon'
                                                            SRC='/webctrl_client/1_0/treeimages/Rminus.gif'></a>
                                                    <font COLOR="#00FFFF" SIZE="2"
                                                        style="display:inline;font-size:10pt;font-face:Times;text-decoration:none;cursor:hand;overflow:hidden;color:#00FFFF;background-color:#08246B;">
                                                        &nbsp;学生使用</font>
                                                </TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><IMG
                                                        align='top' border='0' class='icon'
                                                        SRC='/webctrl_client/1_0/treeimages/T.gif'><a
                                                        href="http://jwgl.szpt.edu.cn/szptjwbsII/Secure2/ChangeKey.aspx">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;密码修改</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><IMG
                                                        align='top' border='0' class='icon'
                                                        SRC='/webctrl_client/1_0/treeimages/T.gif'><a
                                                        href="http://jwgl.szpt.edu.cn/stuinfor/login.aspx">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;学生基本信息</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><IMG
                                                        align='top' border='0' class='icon'
                                                        SRC='/webctrl_client/1_0/treeimages/T.gif'><a
                                                        href="http://jwgl.szpt.edu.cn/tzbm/">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;拓展专业报名系统</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><IMG
                                                        align='top' border='0' class='icon'
                                                        SRC='/webctrl_client/1_0/treeimages/T.gif'><a
                                                        href="http://jwgl.szpt.edu.cn/szptjwbsII/Scoreqry.aspx">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;成绩查询</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><IMG
                                                        align='top' border='0' class='icon'
                                                        SRC='/webctrl_client/1_0/treeimages/T.gif'><a
                                                        href="http://jwgl.szpt.edu.cn/szptjwbsII/CertStuQry.aspx">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;证书查询</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onexpand,0.5')"><IMG
                                                            align='top' border='0' class='icon'
                                                            SRC='/webctrl_client/1_0/treeimages/Tplus.gif'></a><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onselectedindexchange,0,0.5')">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;重修</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onexpand,0.6')"><IMG
                                                            align='top' border='0' class='icon'
                                                            SRC='/webctrl_client/1_0/treeimages/Tplus.gif'></a><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onselectedindexchange,0,0.6')">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;选修</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onexpand,0.7')"><IMG
                                                            align='top' border='0' class='icon'
                                                            SRC='/webctrl_client/1_0/treeimages/Tplus.gif'></a><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onselectedindexchange,0,0.7')">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;选项课</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onexpand,0.8')"><IMG
                                                            align='top' border='0' class='icon'
                                                            SRC='/webctrl_client/1_0/treeimages/Tplus.gif'></a><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onselectedindexchange,0,0.8')">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;辅修</font>
                                                    </a></TD>
                                            </TR>
                                            <TR>
                                                <TD valign='middle'>&nbsp;<IMG align='top' border='0' width='19px'
                                                        height='1px' SRC='/webctrl_client/1_0/treeimages/white.gif'><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onexpand,0.9')"><IMG
                                                            align='top' border='0' class='icon'
                                                            SRC='/webctrl_client/1_0/treeimages/Lplus.gif'></a><a
                                                        href="javascript:__doPostBack('_ctl3:TreeView_stdnt','onselectedindexchange,0,0.9')">
                                                        <font COLOR="#000000" SIZE="2"
                                                            style="display:inline;font-size:10pt;font-face:Times;color:black;text-decoration:none;cursor:hand;overflow:hidden;">
                                                            &nbsp;信息查询</font>
                                                    </a></TD>
                                            </TR>

                                        </table>
                                    </div>
                </P>
                <P>

            </td>
        </tr>
    </table>
    </font>
    </p>
    </td>
    <td width="95%">
        <form name="Form1" method="post" action="RandSchedule.aspx" id="Form1">
            <input type="hidden" name="__EVENTTARGET" value="" />
            <input type="hidden" name="__EVENTARGUMENT" value="" />
            <input type="hidden" name="__VIEWSTATE"
                value="dDwtMTY5OTY1MTc4O3Q8O2w8aTwwPjtpPDI+Oz47bDx0PDtsPGk8Mj47aTwzPjs+O2w8dDw7bDxpPDA+Oz47bDx0PDtsPGk8MD47PjtsPHQ8O2w8aTwxPjs+O2w8dDw7bDxpPDE+O2k8Mz47PjtsPHQ8QDA8cDxwPGw8SGVpZ2h0O1NlbGVjdGVkTm9kZUluZGV4O18hU0I7PjtsPDE8NDIwcHg+OzA7aTwxMjg+Oz4+Oz47Ozs7O0AwPDtAMDxsPGk8MD47PjtsPEAwPEAwPHA8bDxTZWxlY3RlZDs+O2w8bzx0Pjs+Pjs7Ozs+Ozs+Oz47Pjs+Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Oz47Ozs7O0AwPDtAMDxsPGk8MD47PjtsPEAwPEAwPHA8bDxTZWxlY3RlZDs+O2w8bzx0Pjs+Pjs7Ozs+Ozs+Oz47Pjs+Oz47Oz47Pj47Pj47Pj47Pj47dDw7bDxpPDA+Oz47bDx0PDtsPGk8MD47PjtsPHQ8O2w8aTwwPjs+O2w8dDw7bDxpPDE+O2k8Mz47aTw1PjtpPDc+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDU0ODg2OTMyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1Oz4+Oz47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+O3A8bDxvbmNsaWNrO3N0eWxlOz47bDxkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgndGJQcmVmcycpLnN0eWxlLmRpc3BsYXk9J2Jsb2NrJ1w7O2N1cnNvcjpwb2ludGVyXDs7Pj4+Ozs+O3Q8dDw7dDxpPDE2OD47QDxcZTtBY3RpdmVCb3JkZXI7QWN0aXZlQ2FwdGlvbjtBY3RpdmVDYXB0aW9uVGV4dDtBbGljZUJsdWU7QW50aXF1ZVdoaXRlO0FwcFdvcmtzcGFjZTtBcXVhO0FxdWFtYXJpbmU7QXp1cmU7QmVpZ2U7QmlzcXVlO0JsYWNrO0JsYW5jaGVkQWxtb25kO0JsdWU7Qmx1ZVZpb2xldDtCcm93bjtCdXJseVdvb2Q7Q2FkZXRCbHVlO0NoYXJ0cmV1c2U7Q2hvY29sYXRlO0NvbnRyb2w7Q29udHJvbERhcms7Q29udHJvbERhcmtEYXJrO0NvbnRyb2xMaWdodDtDb250cm9sTGlnaHRMaWdodDtDb250cm9sVGV4dDtDb3JhbDtDb3JuZmxvd2VyQmx1ZTtDb3Juc2lsaztDcmltc29uO0N5YW47RGFya0JsdWU7RGFya0N5YW47RGFya0dvbGRlbnJvZDtEYXJrR3JheTtEYXJrR3JlZW47RGFya0toYWtpO0RhcmtNYWdlbnRhO0RhcmtPbGl2ZUdyZWVuO0RhcmtPcmFuZ2U7RGFya09yY2hpZDtEYXJrUmVkO0RhcmtTYWxtb247RGFya1NlYUdyZWVuO0RhcmtTbGF0ZUJsdWU7RGFya1NsYXRlR3JheTtEYXJrVHVycXVvaXNlO0RhcmtWaW9sZXQ7RGVlcFBpbms7RGVlcFNreUJsdWU7RGVza3RvcDtEaW1HcmF5O0RvZGdlckJsdWU7RmlyZWJyaWNrO0Zsb3JhbFdoaXRlO0ZvcmVzdEdyZWVuO0Z1Y2hzaWE7R2FpbnNib3JvO0dob3N0V2hpdGU7R29sZDtHb2xkZW5yb2Q7R3JheTtHcmF5VGV4dDtHcmVlbjtHcmVlblllbGxvdztIaWdobGlnaHQ7SGlnaGxpZ2h0VGV4dDtIb25leWRldztIb3RQaW5rO0hvdFRyYWNrO0luYWN0aXZlQm9yZGVyO0luYWN0aXZlQ2FwdGlvbjtJbmFjdGl2ZUNhcHRpb25UZXh0O0luZGlhblJlZDtJbmRpZ287SW5mbztJbmZvVGV4dDtJdm9yeTtLaGFraTtMYXZlbmRlcjtMYXZlbmRlckJsdXNoO0xhd25HcmVlbjtMZW1vbkNoaWZmb247TGlnaHRCbHVlO0xpZ2h0Q29yYWw7TGlnaHRDeWFuO0xpZ2h0R29sZGVucm9kWWVsbG93O0xpZ2h0R3JheTtMaWdodEdyZWVuO0xpZ2h0UGluaztMaWdodFNhbG1vbjtMaWdodFNlYUdyZWVuO0xpZ2h0U2t5Qmx1ZTtMaWdodFNsYXRlR3JheTtMaWdodFN0ZWVsQmx1ZTtMaWdodFllbGxvdztMaW1lO0xpbWVHcmVlbjtMaW5lbjtNYWdlbnRhO01hcm9vbjtNZWRpdW1BcXVhbWFyaW5lO01lZGl1bUJsdWU7TWVkaXVtT3JjaGlkO01lZGl1bVB1cnBsZTtNZWRpdW1TZWFHcmVlbjtNZWRpdW1TbGF0ZUJsdWU7TWVkaXVtU3ByaW5nR3JlZW47TWVkaXVtVHVycXVvaXNlO01lZGl1bVZpb2xldFJlZDtNZW51O01lbnVUZXh0O01pZG5pZ2h0Qmx1ZTtNaW50Q3JlYW07TWlzdHlSb3NlO01vY2Nhc2luO05hdmFqb1doaXRlO05hdnk7T2xkTGFjZTtPbGl2ZTtPbGl2ZURyYWI7T3JhbmdlO09yYW5nZVJlZDtPcmNoaWQ7UGFsZUdvbGRlbnJvZDtQYWxlR3JlZW47UGFsZVR1cnF1b2lzZTtQYWxlVmlvbGV0UmVkO1BhcGF5YVdoaXA7UGVhY2hQdWZmO1BlcnU7UGluaztQbHVtO1Bvd2RlckJsdWU7UHVycGxlO1JlZDtSb3N5QnJvd247Um95YWxCbHVlO1NhZGRsZUJyb3duO1NhbG1vbjtTYW5keUJyb3duO1Njcm9sbEJhcjtTZWFHcmVlbjtTZWFTaGVsbDtTaWVubmE7U2lsdmVyO1NreUJsdWU7U2xhdGVCbHVlO1NsYXRlR3JheTtTbm93O1NwcmluZ0dyZWVuO1N0ZWVsQmx1ZTtUYW47VGVhbDtUaGlzdGxlO1RvbWF0bztUcmFuc3BhcmVudDtUdXJxdW9pc2U7VmlvbGV0O1doZWF0O1doaXRlO1doaXRlU21va2U7V2luZG93O1dpbmRvd0ZyYW1lO1dpbmRvd1RleHQ7WWVsbG93O1llbGxvd0dyZWVuOz47QDxcZTthY3RpdmVib3JkZXI7YWN0aXZlY2FwdGlvbjtjYXB0aW9udGV4dDtBbGljZUJsdWU7QW50aXF1ZVdoaXRlO2FwcHdvcmtzcGFjZTtBcXVhO0FxdWFtYXJpbmU7QXp1cmU7QmVpZ2U7QmlzcXVlO0JsYWNrO0JsYW5jaGVkQWxtb25kO0JsdWU7Qmx1ZVZpb2xldDtCcm93bjtCdXJseVdvb2Q7Q2FkZXRCbHVlO0NoYXJ0cmV1c2U7Q2hvY29sYXRlO2J1dHRvbmZhY2U7YnV0dG9uc2hhZG93O3RocmVlZGRhcmtzaGFkb3c7YnV0dG9uZmFjZTtidXR0b25oaWdobGlnaHQ7YnV0dG9udGV4dDtDb3JhbDtDb3JuZmxvd2VyQmx1ZTtDb3Juc2lsaztDcmltc29uO0N5YW47RGFya0JsdWU7RGFya0N5YW47RGFya0dvbGRlbnJvZDtEYXJrR3JheTtEYXJrR3JlZW47RGFya0toYWtpO0RhcmtNYWdlbnRhO0RhcmtPbGl2ZUdyZWVuO0RhcmtPcmFuZ2U7RGFya09yY2hpZDtEYXJrUmVkO0RhcmtTYWxtb247RGFya1NlYUdyZWVuO0RhcmtTbGF0ZUJsdWU7RGFya1NsYXRlR3JheTtEYXJrVHVycXVvaXNlO0RhcmtWaW9sZXQ7RGVlcFBpbms7RGVlcFNreUJsdWU7YmFja2dyb3VuZDtEaW1HcmF5O0RvZGdlckJsdWU7RmlyZWJyaWNrO0Zsb3JhbFdoaXRlO0ZvcmVzdEdyZWVuO0Z1Y2hzaWE7R2FpbnNib3JvO0dob3N0V2hpdGU7R29sZDtHb2xkZW5yb2Q7R3JheTtncmF5dGV4dDtHcmVlbjtHcmVlblllbGxvdztoaWdobGlnaHQ7aGlnaGxpZ2h0dGV4dDtIb25leWRldztIb3RQaW5rO2hpZ2hsaWdodDtpbmFjdGl2ZWJvcmRlcjtpbmFjdGl2ZWNhcHRpb247aW5hY3RpdmVjYXB0aW9udGV4dDtJbmRpYW5SZWQ7SW5kaWdvO2luZm9iYWNrZ3JvdW5kO2luZm90ZXh0O0l2b3J5O0toYWtpO0xhdmVuZGVyO0xhdmVuZGVyQmx1c2g7TGF3bkdyZWVuO0xlbW9uQ2hpZmZvbjtMaWdodEJsdWU7TGlnaHRDb3JhbDtMaWdodEN5YW47TGlnaHRHb2xkZW5yb2RZZWxsb3c7TGlnaHRHcmV5O0xpZ2h0R3JlZW47TGlnaHRQaW5rO0xpZ2h0U2FsbW9uO0xpZ2h0U2VhR3JlZW47TGlnaHRTa3lCbHVlO0xpZ2h0U2xhdGVHcmF5O0xpZ2h0U3RlZWxCbHVlO0xpZ2h0WWVsbG93O0xpbWU7TGltZUdyZWVuO0xpbmVuO01hZ2VudGE7TWFyb29uO01lZGl1bUFxdWFtYXJpbmU7TWVkaXVtQmx1ZTtNZWRpdW1PcmNoaWQ7TWVkaXVtUHVycGxlO01lZGl1bVNlYUdyZWVuO01lZGl1bVNsYXRlQmx1ZTtNZWRpdW1TcHJpbmdHcmVlbjtNZWRpdW1UdXJxdW9pc2U7TWVkaXVtVmlvbGV0UmVkO21lbnU7bWVudXRleHQ7TWlkbmlnaHRCbHVlO01pbnRDcmVhbTtNaXN0eVJvc2U7TW9jY2FzaW47TmF2YWpvV2hpdGU7TmF2eTtPbGRMYWNlO09saXZlO09saXZlRHJhYjtPcmFuZ2U7T3JhbmdlUmVkO09yY2hpZDtQYWxlR29sZGVucm9kO1BhbGVHcmVlbjtQYWxlVHVycXVvaXNlO1BhbGVWaW9sZXRSZWQ7UGFwYXlhV2hpcDtQZWFjaFB1ZmY7UGVydTtQaW5rO1BsdW07UG93ZGVyQmx1ZTtQdXJwbGU7UmVkO1Jvc3lCcm93bjtSb3lhbEJsdWU7U2FkZGxlQnJvd247U2FsbW9uO1NhbmR5QnJvd247c2Nyb2xsYmFyO1NlYUdyZWVuO1NlYVNoZWxsO1NpZW5uYTtTaWx2ZXI7U2t5Qmx1ZTtTbGF0ZUJsdWU7U2xhdGVHcmF5O1Nub3c7U3ByaW5nR3JlZW47U3RlZWxCbHVlO1RhbjtUZWFsO1RoaXN0bGU7VG9tYXRvO1RyYW5zcGFyZW50O1R1cnF1b2lzZTtWaW9sZXQ7V2hlYXQ7V2hpdGU7V2hpdGVTbW9rZTt3aW5kb3c7d2luZG93ZnJhbWU7d2luZG93dGV4dDtZZWxsb3c7WWVsbG93R3JlZW47Pj47Pjs7Pjs+Pjs+Pjs+Pjs+Pjs+Pjt0PDtsPGk8MT47aTw0PjtpPDY+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDIwMTnpmYjngoDmnbDlkIzlrabvvIw7Pj47Pjs7Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwxPjtpPDE+O2w8Pjs+Pjs+Ozs7Ozs7Ozs7Oz47bDxpPDA+Oz47bDx0PDtsPGk8MT47PjtsPHQ8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WIm+WuouWei+mhueebruivvueoi182MkY2XzIwMjAxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliJvlrqLlnovpobnnm67or77nqIs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+Wbmzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8OSwxMOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0077yMNi0xMuWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O57Kk5bmzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LuOMTc6NDXlvIDlp4vkuIror77vvIzkuInoioLov57kuIrvvIzkuK3pl7TkuI3kvJHmga/jgILlnLDngrnnlLHogIHluIjlronmjpI7Pj47Pjs7Pjs+Pjs+Pjs+Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8NT47aTwxMDA+O2k8NDE5PjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+O2w8aTwwPjs+O2w8dDw7bDxpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+O2k8OT47aTwxMD47aTwxMT47aTwxMj47aTwxMz47aTwxND47aTwxNT47aTwxNj47aTwxNz47aTwxOD47aTwxOT47aTwyMD47aTwyMT47aTwyMj47aTwyMz47aTwyND47aTwyNT47aTwyNj47aTwyNz47aTwyOD47aTwyOT47aTwzMD47aTwzMT47aTwzMj47aTwzMz47aTwzND47aTwzNT47aTwzNj47aTwzNz47aTwzOD47aTwzOT47aTw0MD47aTw0MT47aTw0Mj47aTw0Mz47aTw0ND47aTw0NT47aTw0Nj47aTw0Nz47aTw0OD47aTw0OT47aTw1MD47aTw1MT47aTw1Mj47aTw1Mz47aTw1ND47aTw1NT47aTw1Nj47aTw1Nz47aTw1OD47aTw1OT47aTw2MD47aTw2MT47aTw2Mj47aTw2Mz47aTw2ND47aTw2NT47aTw2Nj47aTw2Nz47aTw2OD47aTw2OT47aTw3MD47aTw3MT47aTw3Mj47aTw3Mz47aTw3ND47aTw3NT47aTw3Nj47aTw3Nz47aTw3OD47aTw3OT47aTw4MD47aTw4MT47aTw4Mj47aTw4Mz47aTw4ND47aTw4NT47aTw4Nj47aTw4Nz47aTw4OD47aTw4OT47aTw5MD47aTw5MT47aTw5Mj47aTw5Mz47aTw5ND47aTw5NT47aTw5Nj47aTw5Nz47aTw5OD47aTw5OT47aTwxMDA+O2k8MTAxPjs+O2w8dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf44CK57qi5qW85qKm44CL6LWP5p6QXzUzODdfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOOAiue6oualvOaipuOAi+i1j+aekDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeVmeS7mea0nuagoeWMuuW+t+S4mualvDMwMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O5Y2O5Z+6Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlfM2RzbWF45LiJ57u05Yqo55S75Z+656GAX0QzOEZfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDNkc21heOS4iee7tOWKqOeUu+WfuuehgDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS4iee7tOaooeWei+WItuS9nO+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrUHluqc0MjbvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaZj+W8uuWGrDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w856ysM+OAgTTjgIE15ZGo5LiL5Y2I5LiK6IezMTc6MjXvvIzlm5voioLov57kuIo7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9BdXRvQ0FE5py65qKw6auY57qn5Z+56K6tX0IxOTJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPEF1dG9DQUTmnLrmorDpq5jnuqfln7norq07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8OSwxMOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDEwN+acuuaIvzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiH5b+X5Z2aOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxN++8mjQ1LTIw77yaMDDkuInoioLov57kuIo7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9BdXRvQ0FE5py65qKw5Lit57qn5Z+56K6tXzUwNTJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPEF1dG9DQUTmnLrmorDkuK3nuqfln7norq07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw2LDfoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkv6Hmga/mpbw3MDPmnLrmiL87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmZiOefpeazsDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTYtMTjlkajkuIrliLDnrKw46IqCMTc6MjU7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9BdXRvQ0FE5bu6562R57uY5Zu+6auY57qn5oqA5benXzFDMjdfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPEF1dG9DQUTlu7rnrZHnu5jlm77pq5jnuqfmioDlt6c7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Nyw46IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85L+h5oGv5qW8NzA05py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpmYjnu43lkI07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9BdXRvQ0FE5bu6562R57uY5Zu+6auY57qn5oqA5benXzFDMjdfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPEF1dG9DQUTlu7rnrZHnu5jlm77pq5jnuqfmioDlt6c7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85L+h5oGv5qW8NzA05py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpmYjnu43lkI07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9CbGVuZGVy6KeS6Imy6ZuV5aGR5oqA5rOVXzM5MkRfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPEJsZW5kZXLop5LoibLpm5XloZHmioDms5U7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw2LDfoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE05ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuInnu7TmnZDotKjliLbkvZzvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61B5bqnNDI077yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliJjlpKfnlLM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9DNTHljZXniYfmnLrlhaXpl6hfMDU5MV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8QzUx5Y2V54mH5py65YWl6ZeoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWNleeJh+acuuaKgOacrzTvvIjopb/kuL3muZbmoKHljLrmoLznianlm61C5bqnNTA277yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznhorlu7rlubM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDI5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlfQ0FERU5DRemrmOmAn+eUtei3r+adv+iuvuiuoV83RTJGXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxDQURFTkNF6auY6YCf55S16Lev5p2/6K6+6K6hOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDUwNS0x5py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvpDms6I7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDU7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9Db3JlbERSQVflm77lvaLlpITnkIbova/ku7ZfNkY3NV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Q29yZWxEUkFX5Zu+5b2i5aSE55CG6L2v5Lu2Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDksMTDoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkv6Hmga/mpbwzMDbmnLrmiL87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW8oOerizs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Njs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w856ysMTQtMTXlkajku44xN++8mjQ15byA5aeL5LiK6K++77yM5LiJ6IqC6L+e5LiK77yM6KGlMuWtpuaXtjs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX0NvcmVsRFJBV+WbvuW9ouWkhOeQhui9r+S7tl9DODBCXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxDb3JlbERSQVflm77lvaLlpITnkIbova/ku7Y7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw2LDfoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE05ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvrfkuJrmpbwzMjHmnLrmiL87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW8oOiJr+W9qTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8OTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX0RW55+t54mH5Ymq6L6R5LiO5Yi25L2cXzNCRkRfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPERW55+t54mH5Ymq6L6R5LiO5Yi25L2cOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xM+WRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85L+h5oGv5qW8MzAz5py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpn6nmnqs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9JbGx1c3RyYXRvcuWbvuW9ouWItuS9nF9GMzYzXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxJbGx1c3RyYXRvcuWbvuW9ouWItuS9nDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Mi0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW+t+S4mualvDQyMuacuuaIvzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86YOc5bKpOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxNTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX01pY3JvOmJpdOWIm+WuouaKgOacr0JfMUM2N18yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8TWljcm86Yml05Yib5a6i5oqA5pyvQjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlj6/nvJbnqIvpgLvovpHlmajku7bvvIjopb/kuL3muZbmoKHljLrmoLznianlm61C5bqnNjA577yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznjovpnZnpnJ47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlfUGhvdG9zaG9w5Z+656GAXzM2QkZfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFBob3Rvc2hvcOWfuuehgDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDEwMeacuuaIvzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Zu95ZiJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlfUGhvdG9zaG9w5bmz6Z2i5Zu+5b2i5aSE55CG5oqA5pyvX0RFRTNfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFBob3Rvc2hvcOW5s+mdouWbvuW9ouWkhOeQhuaKgOacrzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDUwNuacuuaIvzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8546L5rC45YW0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlfUEtQTee7k+aehOiuvuiuoei9r+S7tuW6lOeUqF9CRUVCXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxQS1BN57uT5p6E6K6+6K6h6L2v5Lu25bqU55SoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xNOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85L+h5oGv5qW8MTA35py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlkJXomY47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDE5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlfUHl0aG9u6K+t6KiA56iL5bqP6K6+6K6h5Y+K5ZyoQUnnrYnpoobln5/nmoTlupTnlKhfQzlCMF8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8UHl0aG9u6K+t6KiA56iL5bqP6K6+6K6h5Y+K5ZyoQUnnrYnpoobln5/nmoTlupTnlKg7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8OSwxMOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDEwNuacuuaIvzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85qyn5p2+Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxN++8mjQ1fjIw77yaMDDkuInoioLov57mjpLjgII7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9Tb2xpZCBXb3Jrc+WfuuehgOW6lOeUqOaKgOacr19BMzcwXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDxTb2xpZCBXb3Jrc+WfuuehgOW6lOeUqOaKgOacrzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDMwNS0y5py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlsKfnh5U7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9Tb2xpZHdvcmtz5o+Q6auY5LiO6K6k6K+BXzFBM0ZfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFNvbGlkd29ya3Pmj5Dpq5jkuI7orqTor4E7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw2LDfoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE05ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkv6Hmga/mpbw3MDLmnLrmiL87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmDreaZk+mcnjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX1VJ6K6+6K6hX0FDRUJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFVJ6K6+6K6hOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b635Lia5qW8MjIw5py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzokovlqJ87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV9VTkktYmlt5bu65qihXzM4QzhfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPFVOSS1iaW3lu7rmqKE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Nyw46IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85bel56iL6aKE566X5qih5oufMe+8iOilv+S4vea5luagoeWMuuagvOeJqeWbrUHluqc2MDXvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOadjuedv+eSnjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX1VOSS1iaW3lu7rmqKFfMzhDOF8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8VU5JLWJpbeW7uuaooTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDEx5ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlt6XnqIvpooTnrpfmqKHmi58x77yI6KW/5Li95rmW5qCh5Yy65qC854mp5ZutQeW6pzYwNe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O552/55KeOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlfd2Vi5YmN56uv572R6aG15Yi25L2cX0JDRjFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPHdlYuWJjeerr+e9kemhteWItuS9nDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznvZHnu5zlt6XnqIvmioDmnK/vvIjopb/kuL3muZbmoKHljLrkv6Hmga/mpbw0MDnvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWImOW5szs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX3dlYuWJjeerr+e9kemhteWItuS9nF9FRThBXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDx3ZWLliY3nq6/nvZHpobXliLbkvZw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86K6h566X5py65aSa5aqS5L2T5oqA5pyv77yI6KW/5Li95rmW5qCh5Yy65L+h5oGv5qW8NTA577yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmm77lu7rljY47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOesrDE3LTE45ZGo5LiK5Yiw56ysN+iKgu+8jOihpTLlrabml7bnmoTor747Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/lt7Toj7Lnibnku7flgLzmipXotYTor77nqItfMjFENV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85be06I+y54m55Lu35YC85oqV6LWE6K++56iLOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xNOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855WZ5LuZ5rSe5qCh5Yy65a2m5oCd5qW8MzI5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpgpPnuqLovok7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDQ1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf54mI55S7XzMxNTNfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeJiOeUuzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeJiOeUu+S4juS4nee9keWNsOWIt++8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrUHluqcxMDHvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWImOilv+ecgTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+eJiOeUu19DMEI0XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzniYjnlLs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855+l6KGM5Zut55S75a6kMe+8iOefpeihjOWbrULluqc1MjBB77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmr5vnoqflqps7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/niYjnlLtfQzBCNF8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w854mI55S7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDcsOOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTHlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOefpeihjOWbreeUu+WupDHvvIjnn6XooYzlm61C5bqnNTIwQe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85q+b56Kn5aqbOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yqe5YWs6L2v5Lu26auY57qn5bqU55SoXzcxNzlfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWKnuWFrOi9r+S7tumrmOe6p+W6lOeUqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDIwMeacuuaIvzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86YOR5p2wOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yqe5YWs6L2v5Lu26auY57qn5bqU55SoLU1PU+W+rui9r+iupOivgV9BMkNBXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlip7lhazova/ku7bpq5jnuqflupTnlKgtTU9T5b6u6L2v6K6k6K+BOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85L+h5oGv5qW8MTA15py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvKDlm63lm607Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDE1LTE35ZGo5LiK5Yiw56ysOOiKgjs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+iDjOWMheept+a4uOS4lueVjOWFpemXqF8wNDMyXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzog4zljIXnqbfmuLjkuJbnlYzlhaXpl6g7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw2LDfoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE05ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlrpjpvpnlsbHmoKHljLrmlZnlrablpKfmpbzpmLYzMDE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW8oOejijE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/ooajppbDml7blsJrkuI7pgInotK1fODkzN18yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86KGo6aWw5pe25bCa5LiO6YCJ6LStOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xNOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Lqn5ZOB5Yib5paw6K6+6K6h5Lit5b+D77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6p+esrDLlsYIyMTjvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmZiOW4g+eRvjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+S6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nF84MDlBXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuqflk4HliJvmhI/orr7orqHkuI7liLbkvZw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xNeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8546v5aKD6Im65pyv5bel6Im65a6e6K6t5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6pzIxOULvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaxn+aVrOiJszs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+S6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nF84MDlBXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuqflk4HliJvmhI/orr7orqHkuI7liLbkvZw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Nyw46IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xNeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8546v5aKD6Im65pyv5bel6Im65a6e6K6t5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6pzIxOULvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaxn+aVrOiJszs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+S6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nF85OUIyXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuqflk4HliJvmhI/orr7orqHkuI7liLbkvZw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTXlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW5v+WRiuiuvuiuoee7mOWbvuWupDLvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61C5bqnNDE4Qu+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O5b+g5paHOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Lqn5ZOB5Yib5oSP6K6+6K6h5LiO5Yi25L2cXzk5QjJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDnvvIwxMS0xNeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86Zm26Im656qR54KJ5a6e6K6t5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6pzExNEHvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOadjuW/oOaWhzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+S6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nF85OUIyXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuqflk4HliJvmhI/orr7orqHkuI7liLbkvZw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Nyw46IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTXlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW5v+WRiuiuvuiuoee7mOWbvuWupDLvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61C5bqnNDE4Qu+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O5b+g5paHOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Lqn5ZOB5Yib5oSP6K6+6K6h5LiO5Yi25L2cXzk5QjJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDnvvIwxMS0xNeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86Zm26Im656qR54KJ5a6e6K6t5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6pzExNEHvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOadjuW/oOaWhzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+S6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nF85OUIyXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuqflk4HliJvmhI/orr7orqHkuI7liLbkvZw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw2LTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOagoeWkluWfuuWcsDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O5b+g5paHOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Lqn5ZOB5Yib5oSP6K6+6K6h5LiO5Yi25L2cXzk5QjJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS6p+WTgeWIm+aEj+iuvuiuoeS4juWItuS9nDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDYtOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85qCh5aSW5Z+65ZywOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmnY7lv6Dmloc7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/kvKDnu5/mrabmnK/vvIjliJ3nuqfvvIlf6L+Q5Yqo6ZifMV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Lyg57uf5q2m5pyv77yI5Yid57qn77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/lm5s7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Mi0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmZiOmbgeadqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86L+Q5Yqo6ZifOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Lyg57uf5q2m5pyv77yI6auY57qn77yJX+i/kOWKqOmYnzFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS8oOe7n+atpuacr++8iOmrmOe6p++8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5ZubOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDItOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlLDmoYLoj4o7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDU7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOi/kOWKqOmYnzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+S8oOe7n+atpuacr++8iOS4ree6p++8iV/ov5DliqjpmJ8xXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkvKDnu5/mrabmnK/vvIjkuK3nuqfvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+Wbmzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855Sw5qGC6I+KOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzov5DliqjpmJ87Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/liJvlrqLlnovpobnnm67or77nqItfNjQ0Ml8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Yib5a6i5Z6L6aG555uu6K++56iLOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/lm5s7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDksMTDoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzljZXniYfmnLrmioDmnK8z77yI6KW/5Li95rmW5qCh5Yy65qC854mp5ZutQuW6pzUwOO+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w854aK5bu65bmzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzMzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85YW35L2T5pe26Ze06ICB5biI5LiO5a2m55Sf5ZWG5a6a44CCOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yib5Lia6IO95Yqb5rKZ55uY5a6e6K6tX0ExRTlfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWIm+S4muiDveWKm+aymeebmOWunuiurTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5YWtOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxLDLoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtNeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b2i5L2T6K6t57uD5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6pzUxMe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w854aK6YGT5LyfOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WIm+S4muiDveWKm+aymeebmOWunuiurV9BMUU5XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliJvkuJrog73lipvmspnnm5jlrp7orq07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+aXpTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTXlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW9ouS9k+iuree7g+WupO+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrULluqc1MTHvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeGiumBk+S8nzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MzA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/liJvkuJrog73lipvmspnnm5jlrp7orq1fQTFFOV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Yib5Lia6IO95Yqb5rKZ55uY5a6e6K6tOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/ml6U7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMsNOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My015ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvaLkvZPorq3nu4PlrqTvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61C5bqnNTEx77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznhorpgZPkvJ87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yib5Lia6IO95Yqb5rKZ55uY5a6e6K6tX0ExRTlfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWIm+S4muiDveWKm+aymeebmOWunuiurTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5YWtOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtNeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b2i5L2T6K6t57uD5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6pzUxMe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w854aK6YGT5LyfOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WIm+S4muiDveWKm+aymeebmOWunuiurV9BMUU5XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliJvkuJrog73lipvmspnnm5jlrp7orq07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+aXpTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MSwy6IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTXlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW9ouS9k+iuree7g+WupO+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrULluqc1MTHvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeGiumBk+S8nzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MzA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/liJvkuJrog73lipvmspnnm5jlrp7orq1fQTFFOV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Yib5Lia6IO95Yqb5rKZ55uY5a6e6K6tOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/lha07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My015ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvaLkvZPorq3nu4PlrqTvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61C5bqnNTEx77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznhorpgZPkvJ87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yib5Lia6IO95Yqb5rKZ55uY5a6e6K6tX0ExRTlfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWIm+S4muiDveWKm+aymeebmOWunuiurTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5pelOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtNeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85b2i5L2T6K6t57uD5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQuW6pzUxMe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w854aK6YGT5LyfOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WIm+S4muiDveWKm+aymeebmOWunuiurV9BMUU5XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliJvkuJrog73lipvmspnnm5jlrp7orq07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+WFrTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Myw06IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTXlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW9ouS9k+iuree7g+WupO+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrULluqc1MTHvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeGiumBk+S8nzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MzA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/liJvmhI/nu5jnlLtfNDMxNl8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Yib5oSP57uY55S7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTHlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeVmeS7mea0nuagoeWMuuW+t+S4mualvDMzMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85byg57uH55KHOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yib5oSP57uY55S7XzQzMTZfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWIm+aEj+e7mOeUuzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDEx5ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlZnku5nmtJ7moKHljLrlvrfkuJrmpbwzMzA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW8oOe7h+eShzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+aYpeeni+aImOWbveWPsuivnV84NjREXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmKXnp4vmiJjlm73lj7Lor507Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8OSwxMOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOilv+S4vea5luagoeWMuuaXpeaWsOalvOmYtjIwMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O5bmzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxN++8mjQ1LTIw77yaMDDkuInoioLov57kuIo7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/ku47orr7orqHoibLlvanliLDmtoLoo4Xorr7orqFfN0MwQl8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LuO6K6+6K6h6Imy5b2p5Yiw5raC6KOF6K6+6K6hOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDksMTDoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE05ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvbHop4blkI7mnJ/liLbkvZzvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61B5bqnMzIw77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvKDoibPlpq47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDE3OjQ1LTIwOjAw5LiJ6IqC6L+e5LiKOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5aSn5a2m55Sf5pe26Ze0566h55CGXzg2MTdfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWkp+WtpueUn+aXtumXtOeuoeeQhjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzopb/kuL3muZbmoKHljLrml6XmlrDmpbzljJcyMDc7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW8oOS6mueQmzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+Wkp+WtpueUn+aXtumXtOeuoeeQhui/m+mYtuivvueoi18yRjlEXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlpKflrabnlJ/ml7bpl7TnrqHnkIbov5vpmLbor77nqIs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Nyw46IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86KW/5Li95rmW5qCh5Yy65pel5paw5qW85YyXMjA3Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvKDkuprnkJs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDI3Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf55S15a2Q5Yi25L2cRElZX0I5RjFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeUteWtkOWItuS9nERJWTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWNleeJh+acuuaKgOacrzPvvIjopb/kuL3muZbmoKHljLrmoLznianlm61C5bqnNTA477yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmnY7nm4rmsJE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDE5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5a6a5ZCR6LaK6YeO77yI5Yid57qn77yJX+i/kOWKqOmYnzFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWumuWQkei2iumHju+8iOWInee6p++8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5ZubOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDItOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvKDpvpk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOi/kOWKqOmYnzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WumuWQkei2iumHju+8iOmrmOe6p++8iV/ov5DliqjpmJ8xXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlrprlkJHotorph47vvIjpq5jnuqfvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+Wbmzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86aKc5rC45rabOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzov5DliqjpmJ87Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/lrprlkJHotorph47vvIjkuK3nuqfvvIlf6L+Q5Yqo6ZifMV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a6a5ZCR6LaK6YeO77yI5Lit57qn77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/lm5s7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Mi0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOminOawuOa2mzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8ODs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86L+Q5Yqo6ZifOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yqo55S755S15b2x5LiO5paH5YyWX0YwRkVfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWKqOeUu+eUteW9seS4juaWh+WMljs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTTlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWQiOaIkOeJueaViOWItuS9nO+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrUHluqczMjjvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmDkemUpueHlTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WKqOeUu+WItuS9nOaKgOacr++8iEZsYXNoKV9GOTI2XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliqjnlLvliLbkvZzmioDmnK/vvIhGbGFzaCk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+WFrTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MSwy6IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTXvvIw3LTnvvIwxMi0xN+WRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85L+h5oGv5qW8MzAx5py65oi/Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzoooHlsI/nuqI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/liqjnlLvliLbkvZzmioDmnK/vvIhGbGFzaClfRjkyNl8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Yqo55S75Yi25L2c5oqA5pyv77yIRmxhc2gpOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/lha07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMsNOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0177yMNy0577yMMTItMTflkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS/oeaBr+alvDMwMeacuuaIvzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86KKB5bCP57qiOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5Yqo54mp5LiW55WMX0I4NkJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWKqOeJqeS4lueVjDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw5LDEw6IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855WZ5LuZ5rSe5qCh5Yy65b635Lia5qW8MjAzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzku6Plu7rlm707Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/liqjniankuJbnlYxfQ0E0NV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Yqo54mp5LiW55WMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeVmeS7mea0nuagoeWMuuW+t+S4mualvDEwNzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Luj5bu65Zu9Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf55+t6KeG6aKR5ouN5pGE5LiO5Ymq6L6RXzAxN0RfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOefreinhumikeaLjeaRhOS4juWJqui+kTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw5LDEw6IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xM+WRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85aqS5L2T562W5YiS5a6k77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQeW6pzMwMu+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8546L5bCP57qiOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuIror77ml7bpl7TvvJoxODowMC0tMjA6MDAsM+iKguivvui/nuS4ijs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+S6jOaJi+i9pumAiei0rV85N0IxXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuozmiYvovabpgInotK07Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85rG96L2m6JCl6ZSA5oqA6IO977yI6KW/5Li95rmW5qCh5Yy65qC854mp5ZutQuW6pzEwNu+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86auY6LCL6I2jOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf6Iqz6aaZ576O5a65XzFBNURfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOiKs+mmmee+juWuuTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDEx5ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzljJblpoborr7orqHlrqTvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61C5bqnMzE1Qe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86buE6IqzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf6Iqz6aaZ576O5a65XzFBNURfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOiKs+mmmee+juWuuTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDEx5ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzljJblpoborr7orqHlrqTvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61C5bqnMzE1Qe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86buE6IqzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf6aOe6ZWW6L+Q5YqoXzFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmjnumVlui/kOWKqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzopb/kuL3muZbmoKHljLrml6XmlrDmpbzljJc2MDc7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmZiOmbgeadqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w856ys5LiA5qyh6K++5Zyo5pel5paw5qW8NjA377yM5Lul5ZCO5Zyo5L2T6IKy6aaG5Ymv6aaG5LiK6K++Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf6Z2e5rSy6byT5YWl6ZeoX0RCNUJfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmdnua0sum8k+WFpemXqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw5LDEw6IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86L65562WOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuIror77lnLDngrnvvJrlpKfov5Dlub/lnLrlkI4y5qW8566h5LmQ5pWZ5a6kOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5L2b5a2m5pm65oWn5LiO5bm456aP5Lq655SfX0NGMjBfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS9m+WtpuaZuuaFp+S4juW5uOemj+S6uueUnzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlZnku5nmtJ7moKHljLrlvrfkuJrmpbwyMDE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW8oOWdpDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MjY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/mnI3oo4XpnaLmlpnnmoTpibTliKvkuI7lupTnlKhfOUFGN18yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pyN6KOF6Z2i5paZ55qE6Ym05Yir5LiO5bqU55SoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xNOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86KW/5Li95rmW5qCh5Yy65pel5paw5qW85Y2XNDAyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzosKLmlofpnZk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDQ4Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5pyN6KOF5L2p6aWw5LiT6aKY6K6+6K6hMl80QUU3XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmnI3oo4XkvanppbDkuJPpopjorr7orqEyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTHlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeVmeS7mea0nuagoeWMuuW+t+S4mualvDMwNzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86JKL5rabOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5pyN6KOF5L2p6aWw5LiT6aKY6K6+6K6hMl80QUU3XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmnI3oo4XkvanppbDkuJPpopjorr7orqEyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDcsOOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTItMTPlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOe6pOe7tOW3peiJuuWunuiureWupO+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrULluqczMTbvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOiSi+a2mzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+acjeijheS9qemlsOS4k+mimOiuvuiuoTJfNEFFN18yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pyN6KOF5L2p6aWw5LiT6aKY6K6+6K6hMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDEyLTEz5ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznuqTnu7Tlt6Xoibrlrp7orq3lrqTvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61C5bqnMzE277yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzokovmtps7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/mnI3oo4XkvanppbDkuJPpopjorr7orqEyXzRBRTdfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOacjeijheS9qemlsOS4k+mimOiuvuiuoTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Nyw46IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMeWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855WZ5LuZ5rSe5qCh5Yy65b635Lia5qW8MzA3Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzokovmtps7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/pkqLnkLTmvJTlpY/mioDms5XvvIjliJ3nuqfvvIlfNTBDRV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86ZKi55C05ryU5aWP5oqA5rOV77yI5Yid57qn77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaVsOeggemSoueQtDLvvIjnlZnku5nmtJ7moKHljLrnn6XooYzlm61B5bqnNealvDUyMTDvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOi/nuiLuTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+mSoueQtOa8lOWlj+aKgOazle+8iOWInee6p++8iV9GQTIwXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpkqLnkLTmvJTlpY/mioDms5XvvIjliJ3nuqfvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Nyw46IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pWw56CB6ZKi55C0Mu+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrUHluqc15qW8NTIxMO+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86L+e6Iu5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf6auY562J5pWw5a2m77yI5LiT5o+S5pys77yJXzRBMzdfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmrmOetieaVsOWtpu+8iOS4k+aPkuacrO+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDYsN+iKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOilv+S4vea5luagoeWMuuaXpeaWsOalvOWMlzQwNjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8572X6JG1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliankuIvlrabml7bogIHluIjkuI7lrabnlJ/llYblrprml7bpl7TooaXor77jgII7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/pq5jnrYnmlbDlrabvvIjkuJPmj5LmnKzvvIlfNzQwNF8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86auY562J5pWw5a2m77yI5LiT5o+S5pys77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNiw36IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86KW/5Li95rmW5qCh5Yy65pel5paw5qW85YyXMzA4Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlurfmmZPnuqI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWJqeS4i+WtpuaXtuiAgeW4iOS4juWtpueUn+WVhuWumuaXtumXtOihpeivvuOAgjs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+mrmOWwlOWkq18xXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpq5jlsJTlpKs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w854aK5bGx6bmwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiK6K++5Zyw54K577ya5Lic5Yy65L2T6IKy6aaG5Ymv6aaGM+alvDs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+mrmOe6p+WKnuWFrOi9r+S7tuW6lOeUqF84Mjk1XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpq5jnuqflip7lhazova/ku7blupTnlKg7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw2LDfoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkv6Hmga/mpbwzMDbmnLrmiL87Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW8oOerizs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w856ysMTYtMTjlkajkuIrliLDnrKw46IqC77yM6KGlM+WtpuaXtjs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+atjOWUseaKgOW3p++8iOWInee6p++8iV8xODM3XzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmrYzllLHmioDlt6fvvIjliJ3nuqfvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86IqC5aWP5LiO5b6L5Yqo77yI55WZ5LuZ5rSe5qCh5Yy655+l6KGM5ZutQeW6pzXmpbw1MjEx77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliJjkuqbnvqQ7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/mrYzllLHmioDlt6fvvIjliJ3nuqfvvIlfNkM4Q18yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85q2M5ZSx5oqA5ben77yI5Yid57qn77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDcsOOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOiKguWlj+S4juW+i+WKqO+8iOeVmeS7mea0nuagoeWMuuefpeihjOWbrUHluqc15qW8NTIxMe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85rGq5pmoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5bel56iL6Im65pyv5qyj6LWPXzRGRDlfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW3peeoi+iJuuacr+aso+i1jzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw3LDjoioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDEx5ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzopb/kuL3muZbmoKHljLrml6XmlrDmpbzljJc0MDI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmZiOmTgeWGsDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/lt6XnqIvoibrmnK/mrKPotY9fNEZEOV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85bel56iL6Im65pyv5qyj6LWPOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTHlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOilv+S4vea5luagoeWMuuaXpeaWsOalvOWMlzQwMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86ZmI6ZOB5YawOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WFrOWFseWkluivremAieS/ru+8iOeUteW9seS4reeahOasp+e+juaWh+WtpuWQjeiRl++8iV8xXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlhazlhbHlpJbor63pgInkv67vvIjnlLXlvbHkuK3nmoTmrKfnvo7mloflrablkI3okZfvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855WZ5LuZ5rSe5qCh5Yy65a2m5oCd5qW8NDI5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmnajlgKk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDI0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5YWs5YWx5aSW6K+t6YCJ5L+u77yI6Leo5paH5YyW5Lqk6ZmF77yJXzFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWFrOWFseWkluivremAieS/ru+8iOi3qOaWh+WMluS6pOmZhe+8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzopb/kuL3muZbmoKHljLrml6XmlrDmpbzljJc0MDc7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOadqOa0izs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NDk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/lhazlhbHlpJbor63pgInkv67vvIjlha3nuqfoi7Hor63vvIlfMV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85YWs5YWx5aSW6K+t6YCJ5L+u77yI5YWt57qn6Iux6K+t77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeVmeS7mea0nuagoeWMuuW+t+S4mualvDMwNTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85L2V5rC45Zu9Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzMzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WFrOWFseWkluivremAieS/ru+8iOaXhea4uOiLseivreinhuWQrOivtOS4juW8guWfn+aWh+WMlu+8iV8xXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlhazlhbHlpJbor63pgInkv67vvIjml4XmuLjoi7Hor63op4blkKzor7TkuI7lvILln5/mlofljJbvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855WZ5LuZ5rSe5qCh5Yy65a2m5oCd5qW8NTAxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmsarmlofmoLw7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/lhazlhbHlpJbor63pgInkv67vvIjllYbliqHoi7Hor63lj6Por63vvIlfMV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85YWs5YWx5aSW6K+t6YCJ5L+u77yI5ZWG5Yqh6Iux6K+t5Y+j6K+t77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeVmeS7mea0nuagoeWMuuWtpuaAnealvDUwMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p2O5aWHOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5YWs5YWx5aSW6K+t6YCJ5L+u77yI5ZWG5Yqh6Iux6K+t5ZCs5Yqb77yJXzFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWFrOWFseWkluivremAieS/ru+8iOWVhuWKoeiLseivreWQrOWKm++8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlZnku5nmtJ7moKHljLrlrabmgJ3mpbw1MTA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOadjuS4uTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WFrOWFseWkluivremAieS/ru+8iOWbm+e6p+iLseivre+8iV8xXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlhazlhbHlpJbor63pgInkv67vvIjlm5vnuqfoi7Hor63vvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8NSw26IqCOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwzLTnvvIwxMS0xOOWRqDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w855WZ5LuZ5rSe5qCh5Yy65a2m5oCd5qW8NTAzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpmYjmtbfnh5U7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOagoeS7u+mAiV/lhazlhbHlpJbor63pgInkv67vvIjoi7HmlofnlLXlvbHkuK3nmoTor63oqIDkuI7mlofljJbvvIlfMV8yMDE5Mjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85YWs5YWx5aSW6K+t6YCJ5L+u77yI6Iux5paH55S15b2x5Lit55qE6K+t6KiA5LiO5paH5YyW77yJOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmmJ/mnJ/kuow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUsNuiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My0577yMMTEtMTjlkag7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOilv+S4vea5luagoeWMuuaXpeaWsOalvOWNlzMwODs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85YiY54ix5a65Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1PjtpPDY+O2k8Nz47aTw4Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzmoKHku7vpgIlf5YWs5YWx5aSW6K+t6YCJ5L+u77yI6Iux6K+t6K+N5rGH77yJXzFfMjAxOTI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWFrOWFseWkluivremAieS/ru+8iOiLseivreivjeaxh++8iTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85pif5pyf5LqMOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw1LDboioI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMtOe+8jDExLTE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlZnku5nmtJ7moKHljLrlvrfkuJrmpbwyMDQ7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOadqOa2jOaziTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2PjtpPDc+O2k8OD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85qCh5Lu76YCJX+WFrOWPuOmHkeiejeS4juWVhuS4muaooeW8j++8iOe9kee7nOivvueoi++8iV82MDNCXzIwMTkyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlhazlj7jph5Hono3kuI7llYbkuJrmqKHlvI/vvIjnvZHnu5zor77nqIvvvIk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaYn+acn+S6jDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8OSwxMOiKgjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8M++8jDE45ZGoOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznlZnku5nmtJ7moKHljLrlrabmgJ3mpbwyMDk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmCk+WJkeWFsDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTMxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlj6YyOOWtpuaXtue6v+S4iuWtpuS5oDs+Pjs+Ozs+Oz4+Oz4+Oz4+Oz4+Oz4+Oz6S6/U+EAUWuFJwQxA2Dus3TIWa3w==" />

            <input type="hidden" name="__VIEWSTATEGENERATOR" value="8A5EFA07" />

            <script language="javascript" type="text/javascript">
< !--
                    function __doPostBack(eventTarget, eventArgument) {
                        var theform;
                        if (window.navigator.appName.toLowerCase().indexOf("microsoft") > -1) {
                            theform = document.Form1;
                        }
                        else {
                            theform = document.forms["Form1"];
                        }
                        theform.__EVENTTARGET.value = eventTarget.split("$").join(":");
                        theform.__EVENTARGUMENT.value = eventArgument;
                        theform.submit();
                    }
// -->
            </script>

            <p><span id="lblUserFLName">2019陈炀杰同学，</span><span id="lblMsg">本学期您的任选课课表如下表所示：</span><a id="Link01"
                    href="Html/补报名提示050304.htm" target="_blank">学生补报名的方法</a>
            <table cellspacing="0" cellpadding="3" rules="rows" bordercolor="#E7E7FF" border="1" id="grdRandSchedule"
                bgcolor="White" width="752">
                <tr bgcolor="#4A3C8C">
                    <td>
                        <font color="#F7F7F7"><b>班级名</b></font>
                    </td>
                    <td>
                        <font color="#F7F7F7"><b>课程</b></font>
                    </td>
                    <td>
                        <font color="#F7F7F7"><b>星期</b></font>
                    </td>
                    <td>
                        <font color="#F7F7F7"><b>节次</b></font>
                    </td>
                    <td>
                        <font color="#F7F7F7"><b>周次</b></font>
                    </td>
                    <td>
                        <font color="#F7F7F7"><b>教室</b></font>
                    </td>
                    <td>
                        <font color="#F7F7F7"><b>教师</b></font>
                    </td>
                    <td width="30">
                        <font color="#F7F7F7"><b>剩余席位</b></font>
                    </td>
                    <td>
                        <font color="#F7F7F7"><b>备注</b></font>
                    </td>
                </tr>
                <tr bgcolor="#E7E7FF">
                    <td>
                        <font color="#4A3C8C">校任选_创客型项目课程_62F6_20201</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">创客型项目课程</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">星期四</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">9,10节</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">3-4，6-12周</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">留仙洞校区德业楼302</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">李粤平</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">32</font>
                    </td>
                    <td>
                        <font color="#4A3C8C">从17:45开始上课，三节连上，中间不休息。地点由老师安排</font>
                    </td>
                </tr>
            </table>
            </p>
            <p>
                <font class="Normal" face="宋体">本学期全校任选课总课表如下：
                    <table cellspacing="0" cellpadding="3" rules="rows" bordercolor="#E7E7FF" border="1"
                        id="grd_RandSchedule_all" bgcolor="White" width="752">
                        <tr bgcolor="#4A3C8C">
                            <td>
                                <font color="#F7F7F7"><b>班级名</b></font>
                            </td>
                            <td>
                                <font color="#F7F7F7"><b>课程</b></font>
                            </td>
                            <td>
                                <font color="#F7F7F7"><b>星期</b></font>
                            </td>
                            <td>
                                <font color="#F7F7F7"><b>节次</b></font>
                            </td>
                            <td>
                                <font color="#F7F7F7"><b>周次</b></font>
                            </td>
                            <td>
                                <font color="#F7F7F7"><b>教室</b></font>
                            </td>
                            <td>
                                <font color="#F7F7F7"><b>教师</b></font>
                            </td>
                            <td width="30">
                                <font color="#F7F7F7"><b>剩余席位</b></font>
                            </td>
                            <td>
                                <font color="#F7F7F7"><b>备注</b></font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_《红楼梦》赏析_5387_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">《红楼梦》赏析</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼302</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李华基</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_3dsmax三维动画基础_D38F_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3dsmax三维动画基础</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">三维模型制作（留仙洞校区知行园A座426）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">晏强冬</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">第3、4、5周下午上至17:25，四节连上</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_AutoCAD机械高级培训_B192_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">AutoCAD机械高级培训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼107机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">万志坚</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">17：45-20：00三节连上</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_AutoCAD机械中级培训_5052_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">AutoCAD机械中级培训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼703机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈知泰</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">16-18周上到第8节17:25</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_AutoCAD建筑绘图高级技巧_1C27_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">AutoCAD建筑绘图高级技巧</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼704机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈绍名</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_AutoCAD建筑绘图高级技巧_1C27_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">AutoCAD建筑绘图高级技巧</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼704机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈绍名</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_Blender角色雕塑技法_392D_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Blender角色雕塑技法</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">三维材质制作（留仙洞校区知行园A座424）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">刘大申</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_C51单片机入门_0591_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">C51单片机入门</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">单片机技术4（西丽湖校区格物园B座506）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊建平</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">29</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_CADENCE高速电路板设计_7E2F_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">CADENCE高速电路板设计</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼505-1机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">徐波</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_CorelDRAW图形处理软件_6F75_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">CorelDRAW图形处理软件</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼306机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张立</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">6</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">第14-15周从17：45开始上课，三节连上，补2学时</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_CorelDRAW图形处理软件_C80B_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">CorelDRAW图形处理软件</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">德业楼321机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张良彩</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_DV短片剪辑与制作_3BFD_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">DV短片剪辑与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-13周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼303机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">韩枫</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_Illustrator图形制作_F363_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Illustrator图形制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">德业楼422机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">郜岩</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">15</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_Micro:bit创客技术B_1C67_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Micro:bit创客技术B</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">可编程逻辑器件（西丽湖校区格物园B座609）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">王静霞</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">31</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_Photoshop基础_36BF_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Photoshop基础</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼101机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">国嘉</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_Photoshop平面图形处理技术_DEE3_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Photoshop平面图形处理技术</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼506机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">王永兴</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_PKPM结构设计软件应用_BEEB_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">PKPM结构设计软件应用</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼107机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">吕虎</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">19</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_Python语言程序设计及在AI等领域的应用_C9B0_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Python语言程序设计及在AI等领域的应用</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼106机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">欧松</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">17：45~20：00三节连排。</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_Solid Works基础应用技术_A370_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Solid Works基础应用技术</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼305-2机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">尧燕</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_Solidworks提高与认证_1A3F_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">Solidworks提高与认证</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼702机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">郭晓霞</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_UI设计_ACEB_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">UI设计</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">德业楼220机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">蒋娟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_UNI-bim建模_38C8_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">UNI-bim建模</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">工程预算模拟1（西丽湖校区格物园A座605）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李睿璞</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_UNI-bim建模_38C8_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">UNI-bim建模</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">工程预算模拟1（西丽湖校区格物园A座605）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李睿璞</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_web前端网页制作_BCF1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">web前端网页制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">网络工程技术（西丽湖校区信息楼409）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">刘平</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_web前端网页制作_EE8A_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">web前端网页制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">计算机多媒体技术（西丽湖校区信息楼509）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">曾建华</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">第17-18周上到第7节，补2学时的课</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_巴菲特价值投资课程_21D5_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">巴菲特价值投资课程</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区学思楼329</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">邓红辉</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">45</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_版画_3153_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">版画</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">版画与丝网印刷（留仙洞校区知行园A座101）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">刘西省</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_版画_C0B4_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">版画</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">知行园画室1（知行园B座520A）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">毛碧媛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_版画_C0B4_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">版画</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">知行园画室1（知行园B座520A）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">毛碧媛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_办公软件高级应用_7179_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">办公软件高级应用</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼201机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">郑杰</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_办公软件高级应用-MOS微软认证_A2CA_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">办公软件高级应用-MOS微软认证</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼105机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张园园</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">15-17周上到第8节</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_背包穷游世界入门_0432_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">背包穷游世界入门</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">官龙山校区教学大楼阶301</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张磊1</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_表饰时尚与选购_8937_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">表饰时尚与选购</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创新设计中心（留仙洞校区知行园B座第2层218）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈布瑾</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_809A_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-15周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">环境艺术工艺实训室（留仙洞校区知行园B座219B）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">江敬艳</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_809A_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-15周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">环境艺术工艺实训室（留仙洞校区知行园B座219B）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">江敬艳</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_99B2_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">广告设计绘图室2（留仙洞校区知行园B座418B）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李忠文</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_99B2_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9，11-15周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陶艺窑炉实训室（留仙洞校区知行园B座114A）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李忠文</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_99B2_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">广告设计绘图室2（留仙洞校区知行园B座418B）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李忠文</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_99B2_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9，11-15周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陶艺窑炉实训室（留仙洞校区知行园B座114A）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李忠文</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_99B2_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">6-8周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">校外基地</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李忠文</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_产品创意设计与制作_99B2_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">产品创意设计与制作</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">6-8周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">校外基地</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李忠文</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_传统武术（初级）_运动队1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">传统武术（初级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期四</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈雁杨</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">运动队</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_传统武术（高级）_运动队1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">传统武术（高级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期四</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">田桂菊</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">运动队</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_传统武术（中级）_运动队1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">传统武术（中级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期四</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">田桂菊</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">运动队</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_创客型项目课程_6442_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创客型项目课程</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期四</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">单片机技术3（西丽湖校区格物园B座508）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊建平</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">33</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">具体时间老师与学生商定。</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期六</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">1,2节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期日</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期日</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3,4节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期六</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期日</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">1,2节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期六</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期日</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_创业能力沙盘实训_A1E9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创业能力沙盘实训</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期六</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3,4节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">形体训练室（留仙洞校区知行园B座511）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊道伟</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">30</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_创意绘画_4316_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创意绘画</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼330</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张织璇</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_创意绘画_4316_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">创意绘画</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼330</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张织璇</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_春秋战国史话_864D_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">春秋战国史话</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼阶202</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李平</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">17：45-20：00三节连上</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_从设计色彩到涂装设计_7C0B_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">从设计色彩到涂装设计</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">影视后期制作（留仙洞校区知行园A座320）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张艳妮</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">17:45-20:00三节连上</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_大学生时间管理_8617_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">大学生时间管理</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北207</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张亚琛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">1</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_大学生时间管理进阶课程_2F9D_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">大学生时间管理进阶课程</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北207</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张亚琛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">27</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_电子制作DIY_B9F1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">电子制作DIY</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">单片机技术3（西丽湖校区格物园B座508）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李益民</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">19</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_定向越野（初级）_运动队1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">定向越野（初级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期四</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张龙</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">运动队</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_定向越野（高级）_运动队1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">定向越野（高级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期四</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">颜永涛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">运动队</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_定向越野（中级）_运动队1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">定向越野（中级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期四</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">2-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">颜永涛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">8</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">运动队</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_动画电影与文化_F0FE_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">动画电影与文化</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">合成特效制作（留仙洞校区知行园A座328）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">郑锦燕</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_动画制作技术（Flash)_F926_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">动画制作技术（Flash)</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期六</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">1,2节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5，7-9，12-17周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼301机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">袁小红</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_动画制作技术（Flash)_F926_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">动画制作技术（Flash)</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期六</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3,4节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-5，7-9，12-17周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼301机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">袁小红</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_动物世界_B86B_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">动物世界</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼203</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">代建国</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_动物世界_CA45_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">动物世界</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼107</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">代建国</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_短视频拍摄与剪辑_017D_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">短视频拍摄与剪辑</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-13周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">媒体策划室（留仙洞校区知行园A座302）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">王小红</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">上课时间：18:00--20:00,3节课连上</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_二手车选购_97B1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">二手车选购</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">汽车营销技能（西丽湖校区格物园B座106）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">高谋荣</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_芳香美容_1A5D_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">芳香美容</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">化妆设计室（留仙洞校区知行园B座315A）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">黄芳</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_芳香美容_1A5D_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">芳香美容</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">化妆设计室（留仙洞校区知行园B座315A）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">黄芳</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_飞镖运动_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">飞镖运动</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北607</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈雁杨</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">第一次课在日新楼607，以后在体育馆副馆上课</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_非洲鼓入门_DB5B_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">非洲鼓入门</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">边策</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">上课地点：大运广场后2楼管乐教室</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_佛学智慧与幸福人生_CF20_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">佛学智慧与幸福人生</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼201</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张坤</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">26</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_服装面料的鉴别与应用_9AF7_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">服装面料的鉴别与应用</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-14周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼南402</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">谢文静</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">48</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_服装佩饰专题设计2_4AE7_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">服装佩饰专题设计2</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼307</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">蒋涛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_服装佩饰专题设计2_4AE7_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">服装佩饰专题设计2</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">12-13周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">纤维工艺实训室（留仙洞校区知行园B座316）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">蒋涛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_服装佩饰专题设计2_4AE7_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">服装佩饰专题设计2</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">12-13周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">纤维工艺实训室（留仙洞校区知行园B座316）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">蒋涛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_服装佩饰专题设计2_4AE7_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">服装佩饰专题设计2</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼307</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">蒋涛</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_钢琴演奏技法（初级）_50CE_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">钢琴演奏技法（初级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">数码钢琴2（留仙洞校区知行园A座5楼5210）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">连苹</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_钢琴演奏技法（初级）_FA20_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">钢琴演奏技法（初级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">数码钢琴2（留仙洞校区知行园A座5楼5210）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">连苹</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_高等数学（专插本）_4A37_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">高等数学（专插本）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北406</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">罗葵</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">剩下学时老师与学生商定时间补课。</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_高等数学（专插本）_7404_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">高等数学（专插本）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北308</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">康晓红</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">剩下学时老师与学生商定时间补课。</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_高尔夫_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">高尔夫</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">熊山鹰</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">10</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">上课地点：东区体育馆副馆3楼</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_高级办公软件应用_8295_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">高级办公软件应用</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6,7节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">信息楼306机房</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">张立</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">第16-18周上到第8节，补3学时</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_歌唱技巧（初级）_1837_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">歌唱技巧（初级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">节奏与律动（留仙洞校区知行园A座5楼5211）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">刘亦群</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_歌唱技巧（初级）_6C8C_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">歌唱技巧（初级）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">节奏与律动（留仙洞校区知行园A座5楼5211）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">汪晨</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_工程艺术欣赏_4FD9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">工程艺术欣赏</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">7,8节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北402</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈铁冰</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">52</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_工程艺术欣赏_4FD9_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">工程艺术欣赏</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北402</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈铁冰</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">52</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（电影中的欧美文学名著）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（电影中的欧美文学名著）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区学思楼429</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">杨倩</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">24</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（跨文化交际）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（跨文化交际）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼北407</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">杨洋</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">49</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（六级英语）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（六级英语）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼305</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">何永国</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">33</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（旅游英语视听说与异域文化）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（旅游英语视听说与异域文化）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区学思楼501</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">汪文格</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（商务英语口语）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（商务英语口语）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区学思楼502</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李奇</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（商务英语听力）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（商务英语听力）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区学思楼510</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">李丹</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（四级英语）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（四级英语）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区学思楼503</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">陈海燕</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（英文电影中的语言与文化）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（英文电影中的语言与文化）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">西丽湖校区日新楼南308</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">刘爱容</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#E7E7FF">
                            <td>
                                <font color="#4A3C8C">校任选_公共外语选修（英语词汇）_1_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公共外语选修（英语词汇）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">5,6节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3-9，11-18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区德业楼204</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">杨涌泉</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">0</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">&nbsp;</font>
                            </td>
                        </tr>
                        <tr bgcolor="#F7F7F7">
                            <td>
                                <font color="#4A3C8C">校任选_公司金融与商业模式（网络课程）_603B_20192</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">公司金融与商业模式（网络课程）</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">星期二</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">9,10节</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">3，18周</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">留仙洞校区学思楼209</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">邓剑兰</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">131</font>
                            </td>
                            <td>
                                <font color="#4A3C8C">另28学时线上学习</font>
                            </td>
                        </tr>
                        <tr align="Right" bgcolor="#E7E7FF">
                            <td colspan="9">
                                <font color="#4A3C8C"><span>1</span>&nbsp;<a
                                        href="javascript:__doPostBack('grd_RandSchedule_all$_ctl104$_ctl1','')">
                                        <font color="#4A3C8C">2</font>
                                    </a>&nbsp;<a
                                        href="javascript:__doPostBack('grd_RandSchedule_all$_ctl104$_ctl2','')">
                                        <font color="#4A3C8C">3</font>
                                    </a>&nbsp;<a
                                        href="javascript:__doPostBack('grd_RandSchedule_all$_ctl104$_ctl3','')">
                                        <font color="#4A3C8C">4</font>
                                    </a>&nbsp;<a
                                        href="javascript:__doPostBack('grd_RandSchedule_all$_ctl104$_ctl4','')">
                                        <font color="#4A3C8C">5</font>
                                    </a></font>
                            </td>
                        </tr>
                    </table>
                </font>
            </p>
        </form>
    </td>
    </tr>
    <tr>
        <td colspan="2" width="100%">
            <table id="_ctl4_pnlFooterGlobal" class="FooterFriends" cellpadding="0" cellspacing="0" border="0"
                width="100%">
                <tr>
                    <td>

                        访问人次累计:
                        <span id="_ctl4_lblCounter">54886932</span>&nbsp;&nbsp; 在线人数:
                        <span id="_ctl4_lblNumOnline">5</span><BR>联系人: (重修等)潘俊新 1078,
                        (学籍等)吴秀明 1080；(技术,流程)刘小华 1246<BR><STRONG>&nbsp;&nbsp;系统开发与维护:
                            深圳职业技术学院电信学院软件工程系、教务处&nbsp;&nbsp; 开始于2004年9月 </STRONG>
                        <BR>
                        <DIV id="tbPrefs" style="DISPLAY: none; TEXT-ALIGN: center">背景色选择：
                            <link rel="stylesheet" href="Style/iestyle.css">
                            <h1>页面错误</h1>
                            <hr />本页面已产生错误，如果情况紧急，您可以与教务处直接联系！<br />本错误产生于如下页面:
                            http://jwgl.szpt.edu.cn/szptjwbsII/RandSchedule.aspx<br />错误信息: <font class="ErrorMessage">
                                类型“DropDownList”的控件“_ctl4_cbBackColor”必须放在具有 runat=server 的窗体标记内。</font>
                            <hr /><b>Stack Trace:</b><br />System.Web.HttpException:
                            类型“DropDownList”的控件“_ctl4_cbBackColor”必须放在具有 runat=server 的窗体标记内。
                            at System.Web.UI.Page.VerifyRenderingInServerForm(Control control)
                            at System.Web.UI.WebControls.DropDownList.AddAttributesToRender(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.RenderBeginTag(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.Render(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderControl(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderChildren(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.RenderContents(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.Render(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderControl(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderChildren(HtmlTextWriter writer)
                            at System.Web.UI.Control.Render(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderControl(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderChildren(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.TableCell.RenderContents(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.Render(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderControl(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderChildren(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.RenderContents(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.Render(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderControl(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.Table.RenderContents(HtmlTextWriter writer)
                            at System.Web.UI.WebControls.WebControl.Render(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderControl(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderChildren(HtmlTextWriter writer)
                            at System.Web.UI.Control.Render(HtmlTextWriter writer)
                            at FriendsReunion.RightPanel.Render(HtmlTextWriter writer)
                            at System.Web.UI.Control.RenderControl(HtmlTextWriter writer)
                            at System.Web.UI.Page.ProcessRequestMain()"""
MAP_DAYS = {
    '星期一': 1,
    '星期二': 2,
    '星期三': 3,
    '星期四': 4,
    '星期五': 5,
    '星期六': 6,
    '星期日': 7,
    '星期天': 7,
}

# def _OptionsListToDict(course_list):
#     """
#     格式化课程List 转换为字典
#     :param course_list: [[course info]...]
#     :return: course dict
#     """
#     re_dict = tree()
#     re_dict.update({
#         "course": {
#             "week": tree()
#         }
#     })
#
#     for course in course_list:
#         base_dict = {
#             "course": course[1],
#             "day": MAP_DAYS[course[2]],
#             "teacher": course[6],
#             "place": course[5],
#             "remark": course[8]
#         }
#         node_str = str(course[3]).replace("节", "")
#         node = node_str.split(",")
#         node = [int(n) for n in node]
#
#         week_str = str(course[4]).replace("周", "")
#         week = week_str.split("，")
#         week = [w for w in week]
#         week_num = []
#         for w in week:
#             num = w.split('-')
#             week_num.extend([i for i in range(int(num[0]), int(num[1]) + 1)])
#
#         for w in week_num:
#             re_dict["course"]["week"][str(w)] = []
#             for n in node:
#                 base = base_dict.copy()
#                 base["node"] = n
#                 re_dict["course"]["week"][str(w)].append(base)
#
#     return re_dict
#
#
# doc_tree = etree.HTML(html_text)
#
# tr = doc_tree.xpath('//table[@id="{}"]/*'.format("grdRandSchedule"))[1:]
# result = []
# for t in tr:
#     fonts = t.xpath('*/font')
#     result.append(["".join(str(font.text).split()) for font in fonts])
#
# d = _OptionsListToDict(result)
# d = json.dumps(d, ensure_ascii=False)
# print(d)

if __name__ == "__main__":
    course = CourseOptions()
    course.login("19240302", "li745789")
    result = course.getOptionsCourse()
    print(json.dumps(result, ensure_ascii=False))
