
         var pathfortrim = location.href;
        if((pathfortrim.match("blonnet.com")) || (pathfortrim.match("thehindubusinessline.com")))
        {
            if(pathfortrim.indexOf(".htm") != -1)
            {
            var trimurl= pathfortrim.substring(pathfortrim.lastIndexOf('/')+1);
            var sid= trimurl.split(".");
                //document.write(trimurl);
			var prod;
				if(pathfortrim.match("/catalyst/"))
					{ var prod="ct"; }
				else if(pathfortrim.match("/ew/"))
					{ var prod="ew"; }
				else if(pathfortrim.match("/mentor/"))
					{ var prod="mn"; }
				else if(pathfortrim.match("/life/"))
					{ var prod="lf"; }
				else if(pathfortrim.match("/manager/"))
					{ var prod="nm"; }
				else if(pathfortrim.match("/iw/"))
					{ var prod="iw"; }
				else
					{ var prod="bl"; }
            var sid1= prod+sid[0];
            window.location.href="http://www.thehindubusinessline.com/template/1-0-1/navigation/markup/archiveUrl.jsp?sourceid=" + sid1;
//document.write(sid1);
//document.write(location.href);
            }
        }
  


    $(document).ready(function() {

        //TABS -- MOST POPULAR
        $("#most-tab-header a").click(function () { return false; });
        $("a#th1").click(function () { showTab(1); });
        $("a#th2").click(function () { showTab(2); });
        showTab(1);

        //TABS -- JOBS/REAL ESTATE
        $("#jobs-tab-header a").click(function () { return false; });
        $("a#th3").click(function () { showJTab(3); });
        $("a#th4").click(function () { showJTab(4); });
        showJTab(3);

        //TABS -- BLOG
        $("#blog-tab-header a").click(function () { return false; });
        $("a#th5").click(function () { showBTab(5); });
        $("a#th6").click(function () { showBTab(6); });
        showBTab(5);

        //CAROUSELS
        $('#multimedia-carousel .mycarousel').jcarousel({scroll: 4,visible: 4});
        $('.multimedia-carousel .mycarousel').jcarousel({scroll: 2});
        $('#topics-carousel .mycarousel,#people-carousel .mycarousel,#video-carousel .mycarousel,#photos-carousel .mycarousel').jcarousel({scroll: 5});
		
		//ARTICLE IMAGE CAROUSELS
        $('#article-carousel .mycarousel').jcarousel({scroll: 1,visible: 1});
        $('.article-carousel .mycarousel').jcarousel({scroll: 1});
        $('#topics-carousel .mycarousel,#people-carousel .mycarousel,#video-carousel .mycarousel,#photos-carousel .mycarousel').jcarousel({scroll: 1});
	//ARTICLE VIDEO CAROUSELS
		$('#videoart-carousel .myVideoCarousel').jcarousel(
			{
				scroll: 1,
				visible: 1
			}
		);
		
		$("#nextVideoBtn").click(
			function()
			{
				var index = BL_VideoPlayer.currentIndex;
				try {
				var isPlaying = flowplayer(index-1).isPlaying();}
				catch(e){
					var isPlaying=false;
				}
				
					if(isPlaying)
					{
						flowplayer(index-1).stop();
					}
				
				BL_VideoPlayer.currentIndex++;
				//alert(BL_VideoPlayer.currentIndex);
				
			}
		);
		
		$("#prevVideoBtn").click(
			function()
			{
				var index = BL_VideoPlayer.currentIndex;
				try {
				var isPlaying = flowplayer(index-1).isPlaying();}
				catch(e){
					var isPlaying=false;
				}
				
				if(isPlaying)
				{
					flowplayer(index-1).stop();
				}
				BL_VideoPlayer.currentIndex--;
				if(BL_VideoPlayer.currentIndex < 1)
				{
					BL_VideoPlayer.currentIndex = 1;
				}
				//alert(BL_VideoPlayer.currentIndex);
				
			}
		);
        //CSS HELP
        $(".columnists-listing-left a:even").css("padding-right", "25px");
        $(".columnists-listing-left a:odd:not(:last)").after("<div class='line two10'></div>");
        $("#getting-around-links a:even").css("padding-right", "20px");
        $(".life-right .pick:last-child").css({border:"none", margin:"0", padding:"0"});

    });

    function showTab(num){
        $("#most-tab .tab").css("display","none");
        $("#most-tab .tab"+num).css("display","block");
        $("#most-tab-header a").removeClass("active");
        $("#most-tab-header a#th"+num).addClass("active");
    }

    function showJTab(num){
        $("#jobs-tab .tab").css("display","none");
        $("#jobs-tab .tab"+num).css("display","block");
        $("#jobs-tab-header a").removeClass("active");
        $("#jobs-tab-header a#th"+num).addClass("active");
    }

    function showBTab(num){
        $("#blog-tab .tab").css("display","none");
        $("#blog-tab .tab"+num).css("display","block");
        $("#blog-tab-header a").removeClass("active");
        $("#blog-tab-header a#th"+num).addClass("active");
    }

//poll start
function callajax(curl,cdata){
  var  callajax ="";
  $.ajax({
    type:"POST",
    url: curl  ,
    data: cdata ,
    async: false,
	success: function(data){callajax = data;  }
    });
	return callajax;
	}
function getCheckedValue(radioObj) {
		if(!radioObj)
			return "";
		var radioLength = radioObj.length;
		if(radioLength == undefined)
			if(radioObj.checked)
				return radioObj.value;
			else
				return "";
		for(var i = 0; i < radioLength; i++) {
			if(radioObj[i].checked) {
				return radioObj[i].value;
			}
		}
		return "";
	}
	function  enableSubmit(artid){
		document.getElementById('subVote' + artid).removeAttribute('disabled');
	}
	
	function vote(artid){
	var svote = getCheckedValue(document.getElementsByName("vote" + artid));
		callajax(publist("url") + "poll/vote.do","mentometerId="+ artid +"&publicationId="+ publist("id") + "&vote=" + svote);
		showresult(artid,"true");
		if((document.cookie.search(artid + "M")) == -1) createCookie("mentometer",artid + "M" + readCookie("mentometer"), 1);
	}
	
	function showresult(artid,result){ 
		var rs = "true";
		if(!result){
			try { 
				if ((document.cookie.search(artid + "M")) == -1){
				$('#poll' + artid).css('display','block');
				} 
				else{$('#poll' + artid).html(callajax(publist("url") + "?service=poll&pollid=" + artid + "&result=" + rs ));
					$('#poll' + artid).css('display','block');
					}
			} catch(err) {} }
			else{
			$('#poll' + artid).html(callajax(publist("url") + "?service=poll&pollid=" + artid + "&result=" + rs ));
			}	
	}
//poll end

// Vuukle comment 

function mostcom(curl,max,cdata){
if ($.browser.msie && parseInt($.browser.version, 10) <= 9) {
   $.getJSON(curl +"&callback=?" , function(data){ var count=0; for (var obj in data){ if (count < (max + 1)){ document.getElementById("mostcom").innerHTML +="<h3><div class='commentspan'><a href='http://" + data[obj].url + "' >" + data[obj].heading + "<\/a><span class='mostCount'>(" + data[obj].count + ")<\/span><\/div><\/h3>" ; count++;}}});
}
else if ('XDomainRequest' in window && window.XDomainRequest !== null) {  
    var xdr = new XDomainRequest();
    xdr.open("get", curl);
    xdr.onload = function () {
        var dom  = new ActiveXObject("Microsoft.XMLDOM"),
            JSON = $.parseJSON(xdr.responseText);
        dom.async = false;
        if (JSON == null || typeof (JSON) == 'undefined') {
            JSON = $.parseJSON(data.firstChild.textContent);
        }
        mostdisplay(JSON,max); 
    };

    xdr.onerror = function() {
        _result = false;  
    };
    xdr.send();
}      
else if(!$.browser.msie ){
    $.ajax({
    type:"GET",
    url: curl  ,
    data: cdata ,
	dataType: "json" ,
    async: false,
	success: function(data){ mostdisplay(data,max); }
    });
}
}
function mostdisplay(data , max){var count=0; for (var obj in data){if (count < (max + 1)){document.getElementById("mostcom").innerHTML +="<h3><div class='commentspan'><a href='http://" + data[obj].url + "' >" + data[obj].heading + "</a><span class='mostCount'>(" + data[obj].count + ")</span></div></h3>" ; count++;}}}

function commentcount(curl,sec,expId){
if ($.browser.msie && parseInt($.browser.version, 10) <= 9) {
   $.getJSON(curl +"&callback=?" , function(data){countlist(data,sec,expId); });
}
else if ('XDomainRequest' in window && window.XDomainRequest !== null) {  
    var xdr = new XDomainRequest();
    xdr.open("get", curl);
    xdr.onload = function () {
        var dom  = new ActiveXObject("Microsoft.XMLDOM"),
            JSON = $.parseJSON(xdr.responseText);
        dom.async = false;
        if (JSON == null || typeof (JSON) == 'undefined') {
            JSON = $.parseJSON(data.firstChild.textContent);
        }
        countlist(JSON,sec,expId); 
    };

    xdr.onerror = function() {
        _result = false;  
    };
    xdr.send();
}      
else if(!$.browser.msie ){
    $.ajax({
    type:"GET",
    url: curl  ,
    data: "" ,
	dataType: "json" ,
    async: false,
	success: function(data){ countlist(data,sec,expId); }
    });
}
}

function countlist(data,sec,expId){  
if (sec){
	for (var obj in data){
		var cname = "comments";	
		if (data[obj] == 1){cname = "comment";}
		if (data[obj] > 0){
		if (expId.indexOf(obj) === -1){$('.count'+obj).html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + data[obj] + "&nbsp;" + cname);}
		else{$('.count'+obj).html("(" + data[obj] + ")");}
		}}
}else{
	for (var obj in data){
	if(data[obj] > 0){$('#count'+obj).html ("(" + data[obj] + ")");}
		if(data[obj] > 0 && data[obj] < 2 ) {
		$('#count'+obj+'a').html('<a href="#comments" class="linkbtn linkbtnl" >View Comment (' + data[obj] + ')</a>');
		}else if (data[obj] > 1){
		$('#count'+obj+'a').html('<a href="#comments" class="linkbtn linkbtnl" >View Comments (' + data[obj] + ')</a>');
		}
	}
 }
}
var BL_VideoPlayer = {currentIndex:1};
//Vuukle comment
//eslider
$(document).ready(function(){$("#cr-slider").show().eSlider({auto: true,continuous: true,numeric: true,speed: 200,pause: 20000,numericId: 'controls'	});	});	
//news flash begin
var newsitems;
var curritem=0;
var iPause=false;
var delay=3000;

$(document).ready(function(){
    $("ul#ticker").addClass("inline")
    var tickerSelector = "ul#ticker li";
    newsitems = $(tickerSelector).hide().hover(
        function(){
            $(this).addClass("hovered");
            iPause=1;
        },
        function(){
            $(this).removeClass("hovered");
            iPause=0;
        }
    ).filter(":eq(0)").show().add(tickerSelector).size();
    setInterval(ticknews,6000); //time in milliseconds
});

function ticknews() {
    // don't run if paused
    if (iPause) return;
    // pause while we do animation
    iPause = true;
    $("#ticker li:eq("+curritem+")").fadeOut("slow",
        function() {
            $(this).hide();
            curritem = ++curritem%newsitems;
            $("#ticker li:eq("+curritem+")").fadeIn("slow",
                function() {
                    iPause = false;
                });
        });
}
//news flash end	
//cookies function  
function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

function eraseCookie(name) {
	createCookie(name,"",-1);
}
