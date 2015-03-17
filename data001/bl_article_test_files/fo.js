//  Copyright (c) 2000-2013 ZEDO Inc. All Rights Reserved.
var q15="http://axp.zedo.com/asw";var e13=new function(){var w3=this;
w3.a7=false;
var zzDtctRules=[{"name":"ShockwaveFlash.ShockwaveFlash.7"},{"name":"ShockwaveFlash.ShockwaveFlash.6"},{"name":"ShockwaveFlash.ShockwaveFlash"}];var zzgetXObj=function(name){var i23=-1;
try{
i23=new ActiveXObject(name);
}
catch(err)
{
i23={
zzactiveXError:true};
}
return i23;
};
w3.e13=function(){
if(navigator.plugins&&navigator.plugins.length>0){
var d1='application/x-shockwave-flash';var c6=navigator.mimeTypes;
if(c6&&c6[d1]&&c6[d1].enabledPlugin&&c6[d1].enabledPlugin.description){
w3.a7=true;
}
}else if(navigator.appVersion.indexOf("Mac")==-1&&window.execScript){
var i44=-1;
for(var i=0;i<zzDtctRules.length&&i44==-1;i++){
var i23=zzgetXObj(zzDtctRules[i].name);
if(!i23.zzactiveXError){
w3.a7=true;
}}}
}();
};
get_flash_bit=function(){
var n4=navigator.userAgent.toLowerCase();var c21=(n4.indexOf('mac')!=-1);var i21=parseInt(navigator.appVersion);
var c22=(!c21&&(n4.indexOf('opera')==-1)&&(n4.indexOf('msie')!=-1)&&(i21>=4)&&(n4.indexOf('webtv')==-1
)&&(n4.indexOf('msie 4')==-1));
var p19=navigator.javaEnabled();var q4=1;
if(p19){q4 |=4;}
if(e13.a7){q4 |=8;}
if(c22){
if(document.documentElement){
document.documentElement.style.behavior='url(#default#clientCaps)';
if(document.documentElement.connectionType=='lan'){
q4 |=16;
}}
else if(document.body){
document.body.style.behavior='url(#default#clientCaps)';
if(document.body.connectionType=='lan'){
q4 |=16;
}}}
return q4;
};
var y13=get_flash_bit();
if(y13==null){
y13='';
}

if(typeof zflag_vals!='undefined'&&typeof zflag_vals.c!='undefined'){
var zflag_cid=zflag_vals.c;}
if(typeof zflag_vals!='undefined'&&typeof zflag_vals.s!='undefined'){
var zflag_sid=zflag_vals.s;}
var v12=0;var a0='';var a6=0;var a6=0;var d48;var p46;var n47;var t47;var i47;var z47;var w47='';var o16='0';var d13=0;var c30='';var zd_$='';var a7=0;var c26='';
var y29='';var i37="";var z34='';var p36='';var d18=new Array();var i13='';var p34=0;var i30='';var v10="";var n30="";var d30="";var y16="";var q29="";var t24="";var d31="";var p24=new Array();
var z38=new Array();var e22=new Array();var w32=0;var r19="";var q19="";var r36="";
if(typeof zflag_ct!='undefined'){
r36=encodeURI(zflag_ct);
zflag_ct="";
}
if(typeof zflag_nid!='undefined'){
v12=zflag_nid;
zflag_nid=0;
}
if(typeof zflag_charset!='undefined'){
a0="charset="+zflag_charset;
zflag_charset="";
}
if(typeof zflag_sid!='undefined'){
a6=zflag_sid;
}
if(typeof zflag_pbnw!='undefined'){
v10+="&pn="+zflag_pbnw;
zflag_pbnw=0;
}
if(typeof zflag_6!='undefined'){
v10+="&6="+zflag_6;
zflag_6=0;
}
if(typeof zflag_pbad!='undefined'){
v10+="&pa="+zflag_pbad;
zflag_pbad=0;
}
if(typeof zflag_pbch!='undefined'){
if(zflag_pbch.indexOf("/")!=-1){
var t45=zflag_pbch.substr(0,zflag_pbch.indexOf("/"));
v10+="&pc="+t45;
}
else{
v10+="&pc="+zflag_pbch;
}
zflag_pbch="0";
}
if(typeof zflag_pbr!='undefined'){
v10+="&pr="+zflag_pbr;
zflag_pbr=0;
}
if(typeof zflag_pbsid!='undefined'){
v10+="&ps="+zflag_pbsid;
}
if(typeof zflag_tmy!='undefined'){
n30+="&tmy="+zflag_tmy;
zflag_tmy=0;
}
if(typeof zflag_cid!='undefined'){
o16=zflag_cid;
if(o16<0||o16>999999){
o16=0;
}}
if(typeof zflag_chanlimits!='undefined'){
p34=zflag_chanlimits;
zflag_chanlimits=0;
}
if(typeof zflag_sz!='undefined'){
d13=zflag_sz;
if(d13<0||d13>95){
d13=0;
}
zflag_sz=0;
}
if(typeof zflag_alter_sz!='undefined'){
y16=zflag_alter_sz;
if(y16<0||y16>95){
y16=0;
}
zflag_alter_sz=0;
}
if(typeof zflag_kw!='undefined'){
zflag_kw=zflag_kw.replace(/&/g,'zzazz');
c30=zflag_kw;
zflag_kw="";
}
if(typeof zflag_$!='undefined'){
zd_$=zflag_$;
zflag_$='';
}
if(typeof zflag_geo!='undefined'){
if(!isNaN(zflag_geo)){
c26="&gc="+zflag_geo;
zflag_geo=0;
}}
if(typeof zflag_param!='undefined'){
i37="&p="+zflag_param;
zflag_param="";
}
if(typeof zflag_click!='undefined'){
zzTrd=encodeURI(zflag_click);
y29='&l='+zzTrd;
zflag_click="";
}
if(typeof zflag_ad_title!='undefined'){
zzTitle=escape(zflag_ad_title);
i30='&t='+zzTitle;
zflag_ad_title="";
}
if(typeof zflag_hasAd!='undefined'){
z34='&y='+zflag_hasAd;
}
if(typeof zflag_num!='undefined'){
p36=zflag_num;
zflag_num=0;
}
if(typeof zflag_ck!='undefined'){
i13='&ck='+zflag_ck;
zflag_ck=0;
}
if(typeof zflag_message_transport!='undefined'){
d30=zflag_message_transport;
zflag_message_transport=0;
}
if(typeof zflag_multi_param!='undefined'){
q29="&mp="+zflag_multi_param;
zflag_multi_param="";
}
if(typeof zflag_smooth!='undefined'){
t24+="&ssm="+zflag_smooth;
}
if(typeof zflag_slide_speed!='undefined'){
t24+="&ssp="+zflag_slide_speed;
}
if(typeof zflag_slider_close_text!='undefined'){
t24+="&sct="+zflag_slider_close_text;
}
if(typeof zflag_page!='undefined'){
r19=zflag_page;
zflag_page=='';
}
if(typeof zflag_ref!='undefined'){
q19=zflag_ref;
zflag_ref='';
}
var d18="d1,d2,d3,d4,d5,d6,d7,d8,d9,da,db,dc,dd,de,df".split(",");
function F14(){
var a19=new Array();
for(var i=0;i<d18.length;i++){
a19[i]=d18[i].substring(1);
}
return a19;
}
function F12(){
var e25=d18;var n6=new Array();var p13=new RegExp(",","g");
for(var i=0;i<e25.length;i++){
if(eval('typeof(zflag_'+d18[i]+')!="undefined"')){
n6[i]=eval('zflag_'+d18[i]);
if(n6[i]!=""){
n6[i]=n6[i].replace(p13,"Z");
}}}
return n6;
}
z38=F14();
e22=F12();
for(var i=0;i<e22.length;i++){
if(e22[i]!=""&&typeof e22[i]!='undefined'){
p24[p24.length]=z38[i]+":"+e22[i];
}}
if(p24.length!=0){
d31='&dm='+p24;
}
var zzStr='';
if(typeof zzCountry=='undefined'){
var zzCountry=255;}
if(typeof zzMetro=='undefined'){
var zzMetro=0;}
if(typeof zzState=='undefined'){
var zzState=0;}var zzSection=a6;var zzPbNId=p46;var zzPbEId=n47;var zzPbAId=t47;var zzPbCId=i47;var zzPbGeoLvl=z47;var zzPbk=w47;
if(typeof zzPbk=='undefined'){
zzPbk=-1;
}
var zzPbSId=d48;var zzD=window.document;var zzRand=(Math.floor(Math.random()* 1000000)% 10000);var zzCustom='';var zzPat='';var zzSkip='';var zzExp='';var zzTrd='';var zzPos=0;var zzNw=0;var zzCh=0;
var zzDmCodes=new Array();var zzDmValues=new Array();var zzBr=99;var zzLang=99;var zzAGrp=0;var zzAct=new Array();var zzActVal=new Array();
if(y13<0||y13>31){
y13=1;
}
var q10=new Array();
function B0(zp_label){
if(!q10[zp_label]){
var i35=document.cookie;var o7=new Array();var y14=new Array();
o7=i35.split(';');
var w33=(o7!=null)?o7.length:0;
for(var i=0;i<w33;i++){
o7[i]=o7[i].replace(/^\s/,'');
y14=o7[i].split('=');
q10[y14[0]]=y14[1];
}}
if(q10[zp_label]){
return q10[zp_label];
}else{
return '';
}}
function F56(){
var r42=new Date();var i48=new Date(r42.getFullYear(),0,1,0,0,0,0);var a44=new Date(r42.getFullYear(),6,1,0,0,0,0);var o47=Math.max(i48.getTimezoneOffset(),a44.getTimezoneOffset());
return-o47/60;
}
w32=F56();
function F21(isJSTag){
var t30='';
try{
if(isJSTag){
t30=(typeof(location.href)=='undefined'?"":encodeURI(location.href.split("?")[0]));
}else{
t30=(typeof(document.referrer)=='undefined'?"":encodeURI(document.referrer.split("?")[0]));
}
}catch(err){}
return t30;
}
function U18(isJSTag){
var n38='';
try{
if(isJSTag){
n38=(typeof(document.referrer)=='undefined'?"":encodeURI(document.referrer.split("?")[0]));
}
}catch(e){}
return n38;
}

z0=q15+'/fm.js?c='+o16+'&a='+p34+'&f='+p36+'&n='+v12
+'&r='+y13+'&d='+d13+'&adm='+y16+'&q='+c30+'&$='+zd_$+v10+n30+'&s='+a6+c26+i37+y29+z34+i30+
'&ct='+r36+d31+'&z='+Math.random()+'&tt=0'+q29+'&tz='+w32+'&pu='+((r19!='')?encodeURI(r19.split("?")[0]):F21(true))+'&ru='+((q19!='')?encodeURI(q19.split("?")[0]):U18(true));
z0='<scr'+'ipt language="javascript" src="'+z0+'" '+a0+'></scr'+'ipt>';
var v19=B0("ZEDOIDA");
if(!(v19=="OPT_OUT"&&d13==15)){
document.write(z0);
}