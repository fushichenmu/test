load "/data/cipas/java/tomcat/tomcat-service/webapps/WMFS_SERVICE_1.0/WEB-INF/classes/extComponent/ncl_component/util/tools.ncl"
load "/data/cipas/java/tomcat/tomcat-service/webapps/WMFS_SERVICE_1.0/WEB-INF/classes/extComponent/ncl_component/util/datatools.ncl"
load "/data/cipas/java/tomcat/tomcat-service/webapps/WMFS_SERVICE_1.0/WEB-INF/classes/extComponent/ncl_component/util/stationdata.ncl"

;******************************************************************************
;绘制中国区域无mask，自带标题、logo，可接三维或四维数据
;******************************************************************************
undef ("AddChar")
;添加图例上的汉字
procedure AddChar(InputFile,InputName,fontfile,location,fontsize,char)
;inputimage:图片路径
;fontfile:字体路径
;location:添加位置（eg:+1000+800）
;fontsize:字体大小
;char:字符串
begin
    cmd = "mogrify -font "+fontfile+" -pointsize " + fontsize + " -annotate " + location +" " + char + " " + InputFile+InputName
    system(cmd)
end

undef("draw_chpic")
function draw_chpic(data,colorcfg,size,picoutpath,picname)
begin
    ;图片像素大小，长和宽
	nsize = tofloat(str_split(size,"x"))
    imgWidth = nsize(0)
    imgHeight = nsize(1)
    wks_type = "png"
    wks_type@wkWidth = max(nsize)
    wks_type@wkHeight = min(nsize)
    checkOrCreateDir(picoutpath)
    cmap = getColorMap(colorcfg)
    wks = gsn_open_wks(wks_type, picoutpath+picname)
    gsn_define_colormap(wks, cmap)


    res                         = True
	res@gsnMaximize                = False
	res@gsnDraw                    = False
	res@gsnFrame                   = False
	res@gsnAddCyclic            = False	
    res@mpProjection = "LambertConformal" ;"LambertEqualArea"
	res@mpGridAndLimbOn = False
	res@mpLambertMeridianF = 105.0
	res@mpLimitMode = "Corners "
	res@mpLambertParallel1F = 25     ;Default: .001 
	res@mpLambertParallel2F = 48   ;Default: 89.999
	res@mpPerimOn 				   = True
	res@mpPerimLineThicknessF = 1
	res@mpGridLineDashPattern= 5
	res@mpGridLineThicknessF = 0.5
	
	res@mpLeftCornerLatF = 13.2578
	res@mpRightCornerLatF = 50.6752
	res@mpLeftCornerLonF = 78.9951
	res@mpRightCornerLonF = 148.8066
	
	res@vpXF                 = 0.
	res@vpYF                 = 1.
	res@vpWidthF             = 1.     
	res@vpHeightF            = 1.
	

	res@mpFillOn                   = True
	res@mpDataSetName              = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/basedata/Earth..4"
	res@mpDataBaseVersion          = "MediumRes" ; or "Ncarg4_1"
	res@mpAreaMaskingOn            = True
	res@mpMaskAreaSpecifiers       = (/"China"/)
	res@mpMaskOutlineSpecifiers        = (/"China"/)
    
	res@mpLandFillColor            = (/255.0/255,255.0/255,254.0/255/)
	res@mpInlandWaterFillColor     = (/255.0/255,255.0/255,254.0/255/)
	res@mpOceanFillColor           = (/255.0/255,255.0/255,254.0/255/)
	res@mpOutlineBoundarySets      = "NoBoundaries"
	res@mpNationalLineColor        = (/255.0/255,255.0/255,254.0/255/)
	res@mpGeophysicalLineColor     = (/255.0/255,255.0/255,254.0/255/)
	res@mpNationalLineThicknessF   = 0.
;---------------------------------------------------------------
;	set for the plot		
	cnLevels = getColorValueDef(colorcfg)
	res@tmXBOn                   = False 
	res@tmXTOn                   = False
	res@tmYLOn                   = False
	res@tmYROn                   = False	
	;等值线属性
	res@cnFillColors           = getColorOrder(colorcfg)
	res@cnLevelSelectionMode   = "ExplicitLevels"
	res@cnInfoLabelOn		   = False 		;不显示标签
	res@cnLevels               = cnLevels
	;res@cnSmoothingOn          = True 		;平滑
	;res@cnSmoothingTensionF    = 0.1
	;res@cnMissingValFillColor = "grey"
	;res@cnConstFEnableFill        = True  ;缺测填充（废弃）
    ;res@cnNoDataLabelOn           = False 
    ;res@cnConstFLabelOn           = False 
	
	res@cnFillOn                   = True
	res@cnFillDrawOrder            = "PreDraw"
	res@cnLinesOn                  = False             
	res@cnLevelSpacingF            = 20. 
            
	;res@gsnSpreadColors            = True   
	res@cnLineLabelsOn       = False   ;关闭等值线标注说明
	res@pmTickMarkDisplayMode      = "Always"
	res@lbLabelBarOn = False ;NCL自带图例不绘
	res@gsnRightString             = " " ;坐标轴标签名
	res@gsnLeftString             = " "
	
	map = gsn_csm_contour_map(wks,data,res)
	;叠加图片掩膜
	; if(isStrSubset(picname,"TK") .and. isStrSubset(picname,"850"))then
		; shpFileym = "/nfsshare/cdbdata/algorithm/conductor/WMFS/airPollution/shp/"
		; ymres = True
		; ymres@gsFillColor = "grey"
		; plotym = gsn_add_shapefile_polygons(wks,map,shpFileym+"h850.shp",ymres)
	; end if
	; if(isStrSubset(picname,"TK") .and. isStrSubset(picname,"700"))then
		; shpFileym = "/nfsshare/cdbdata/algorithm/conductor/WMFS/airPollution/shp/"
		; ymres = True
		; ymres@gsFillColor = "grey"
		; plotym = gsn_add_shapefile_polygons(wks,map,shpFileym+"h700.shp",ymres)
	; end if
	; if(isStrSubset(picname,"RH") .and. isStrSubset(picname,"1000"))then
		; shpFileym = "/nfsshare/cdbdata/algorithm/conductor/WMFS/airPollution/shp/"
		; ymres = True
		; ymres@gsFillColor = "grey"
		; plotym = gsn_add_shapefile_polygons(wks,map,shpFileym+"h1000.shp",ymres)
	; end if
	; if(isStrSubset(picname,"RH") .and. isStrSubset(picname,"850"))then
		; shpFileym = "/nfsshare/cdbdata/algorithm/conductor/WMFS/airPollution/shp/"
		; ymres = True
		; ymres@gsFillColor = "grey"
		; plotym = gsn_add_shapefile_polygons(wks,map,shpFileym+"h850.shp",ymres)
	; end if
	; if(isStrSubset(picname,"RH") .and. isStrSubset(picname,"700"))then
		; shpFileym = "/nfsshare/cdbdata/algorithm/conductor/WMFS/airPollution/shp/"
		; ymres = True
		; ymres@gsFillColor = "grey"
		; plotym = gsn_add_shapefile_polygons(wks,map,shpFileym+"h700.shp",ymres)
	; end if

	shpFile = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/map/"
	;河流 
	river                          = True
	river@gsLineThicknessF         = 1.0       
	river@gsLineColor              = "blue"
	plotrv = gsn_add_shapefile_polylines(wks,map,shpFile+"HYDL.shp",river)
	;省份
	prres=True
	prres@gsLineThicknessF = 1.0       
	prres@gsLineColor = "black"
	prres@gsLineDashPattern = 0
	plotcn4 = gsn_add_shapefile_polylines(wks,map,shpFile+"BOUL_S.shp",prres)
	;海岸线 
	dqres=True
	dqres@gsLineThicknessF = 1.0      
	dqres@gsLineColor = (/0.0/255,0.0/255,153.0/255/)
	plotcn5 = gsn_add_shapefile_polylines(wks,map,shpFile+"HAX.shp",dqres)
	;南海
	nres=True
	nres@gsLineThicknessF = 1.0     
	nres@gsLineColor = (/0.0/255,0.0/255,153.0/255/)
	plotcn6 = gsn_add_shapefile_polylines(wks,map,shpFile+"nh/HFCP.shp",nres)
	;香港
	xgres=True
	xgres@gsLineThicknessF = 2.0      
	xgres@gsLineColor = "black"
	xgres@gsLineDashPattern = 2
	plotcn7 = gsn_add_shapefile_polylines(wks,map,shpFile+"BOUL_S2.shp",xgres)
	;已定国界
	cnres      = True      
	cnres@gsLineThicknessF = 2.0       
	cnres@gsLineColor = "black"
	cnres@gsLineDashPattern = 0
	plotcn1 = gsn_add_shapefile_polylines(wks,map,shpFile+"BOUL_GY.shp",cnres)
	;未定国界
	wnres      = True      
	wnres@gsLineThicknessF = 2.0       
	wnres@gsLineColor = "black"
	wnres@gsLineDashPattern = 1
	plotcn2 = gsn_add_shapefile_polylines(wks,map,shpFile+"BOUL_GW.shp",wnres)
	
	;南海小地图 
	nhres                          = res
	nhres@gsnMaximize              = False

	nhres@vpHeightF                = 0.18    
	nhres@vpWidthF                 = 0.18
  
	nhres@mpLeftCornerLatF = 2.8
	nhres@mpRightCornerLatF = 23.3
	nhres@mpLeftCornerLonF = 106.7
	nhres@mpRightCornerLonF = 126.6
  
  	nhres@tmXBOn                   = False 
	nhres@tmXTOn                   = False
	nhres@tmYLOn                   = False
	nhres@tmYROn                   = False

	nhres@lbLabelBarOn             = False

	nhres@gsnLeftString            = ""
	nhres@gsnRightString           = ""
	nhres@gsnCenterString          = ""

	map_nanhai = gsn_csm_contour_map(wks,data,nhres)
	
;对shp格式数据重设置属性
	dqres@gsLineThicknessF = 1.0 
	cnres@gsLineThicknessF = 1.0 
	wnres@gsLineThicknessF = 1.0 
  
	plotcn1_nh = gsn_add_shapefile_polylines(wks,map_nanhai,shpFile+"nh/HFCP.shp",nres) ;南海
	plotcn2_nh = gsn_add_shapefile_polylines(wks,map_nanhai,shpFile+"nh/BOUL_G.shp",cnres) ;已定国界
	plotcn4_nh = gsn_add_shapefile_polylines(wks,map_nanhai,shpFile+"BOUL_S.shp",prres) ;已定省界
	plotcn6_nh = gsn_add_shapefile_polylines(wks,map_nanhai,shpFile+"nh/HAX.shp",dqres) ;海岸线
	plotcn5_nh = gsn_add_shapefile_polylines(wks,map_nanhai,shpFile+"nh/BOUL_S2.shp",prres) ;香港
	;plotcn7_nh = gsn_add_shapefile_polylines(wks,map_nanhai,shpFile+"nh/BOUL_JDX.shp",cnres)
	plotcn8_nh = gsn_add_shapefile_polylines(wks,map_nanhai,shpFile+"nh/BOUL_GY.shp",cnres)
	; if(isStrSubset(picname,"RH") .and. isStrSubset(picname,"1000"))then
		; plotym_nh = gsn_add_shapefile_polygons(wks,map_nanhai,shpFileym+"h1000.shp",ymres)
	; end if
	;加比例尺文字
	txres = True
	txres@txFontHeightF = 0.008
	txres@txFontColor = "black"
	dum1 = gsn_add_text(wks,map_nanhai,"1:40 000 000",118,3,txres)

;加载南海的位置
	adres                          = True
	adres@amParallelPosF           = 0.489247 ; -0.5 is the left edge of the plot.
	adres@amOrthogonalPosF         = 0.4856322  ; -0.5 is the top edge of the plot.
	adres@amJust                   = "BottomRight"

	plotnh = gsn_add_annotation(map,map_nanhai,adres)
	
	;添加图例
	nboxes = dimsizes(res@cnFillColors)
	labels = new((/nboxes/),"string")
	;有缺测值时
	if(isStrSubset(picname,"RH") .or. isStrSubset(picname,"TK"))then
		labels(0)="NoData"
		labels(1)="<"+cnLevels(1)
		labels(nboxes-1)=">"+cnLevels(nboxes-2)
		do i=2,nboxes-2
			labels(i)=cnLevels(i-1)+"~F34~*~F~"+cnLevels(i)
		end do
	;无缺测值时
	else
		labels(0)="<"+cnLevels(0)
		labels(nboxes-1)=">"+cnLevels(nboxes-2)
		do i=1,nboxes-2
			labels(i)=cnLevels(i-1)+"~F34~*~F~"+cnLevels(i)
		end do
	end if
	
	
  
	lbres                    = True          ; labelbar only resources
	lbres@lbAutoManage       = False          ; Necessary to control sizes
	lbres@lbLabelAlignment = "BoxCenters"
	lbres@lbTitleString = "fads"
	lbres@lbTitleFontHeightF = 0.035
	lbres@lbTitleFontColor  = (/255.0/255,255.0/255,254.0/255/)
	lbres@lbPerimOn         = True
	lbres@lbPerimColor  =  "black"
	lbres@lbPerimThicknessF = 2
	lbres@lbJustification = "CenterLeft"
	lbres@vpWidthF           = 0.11     ; labelbar width
	lbres@vpHeightF          = 0.022*0.868*(nboxes+3-(nboxes-5)/2.8)   ; labelbar height
	lbres@lbBoxMajorExtentF  = 0.8         ; puts space between color boxes
	lbres@lbFillColors       = res@cnFillColors ; labelbar colors
	lbres@lbMonoFillPattern  = True          ; Solid fill pattern
	if(isStrSubset(picname,"TK"))then
		lbres@lbLabelFontHeightF = 0.009          ; font height. default is small
	else
		lbres@lbLabelFontHeightF = 0.009677
	end if
	lbres@lbLabelJust        = "CenterLeft"  ; left justify labels
;绘制自定义图例
	lbid = gsn_create_labelbar(wks,nboxes,labels,lbres)
	; amParallelPosF/amOrthogonalPosF                                       ;
	   ; 0.0/ 0.0  -  annotation in dead center of plot
	   ; 0.5/ 0.5  -  annotation at bottom right of plot
	   ; 0.5/-0.5  -  annotation at top right of plot
	  ; -0.5/-0.5  -  annotation at top left of plot
	  ; -0.5/ 0.5  -  annotation at bottom left of plot	
	amres                  = True
	amres@amJust           = "BottomLeft"
	amres@amParallelPosF   = -0.489247
	amres@amOrthogonalPosF = 0.4856322
	annoid = gsn_add_annotation(map,lbid,amres)  
  
	;添加南海比例尺
	txres = True
	txres@txFontHeightF = 0.012097
	txres@txFontColor = "black"
	dum = gsn_add_text(wks,map,"Scale 1:20 000 000",95,17,txres)   
	draw(map)
    frame(wks)
    transparentBkColor("white -crop 930x695.912211+0+117.0438945", picoutpath+picname+".png")	
    return nboxes
end






begin    
	; forecastTime = "2019/04/18"
    ; timeType = "five" ;"five","week"
	; timeRange = "1-2" ;"1-1"
    ; var = "prate"
	; height = ""
	; colorcfg  = "/nfsshare/testSH/air/scripts/ini/prate.ini"
    ; picoutPath = "/nfsshare/testSH/air/output/"
    ; picName  = "prate"
	; units = "毫米"
	
	forecastTime = readParams(paramFile,"forecastTime")
    timeType = readParams(paramFile,"timeType") ;"five","week"
	timeRange = readParams(paramFile,"timeRange") ;"1-1"
    var = readParams(paramFile,"var")
	height = readParams(paramFile,"height")
	colorcfg  = readParams(paramFile,"colorcfg")
	if(var.eq."tk" .and. height.eq."200")then
		colorcfg  = "/nfsshare/cdbdata/data/airPollution/ini/tk200.ini"
	end if
    picoutPath = readParams(paramFile,"picoutPath")
    picName  = readParams(paramFile,"picName")
	;units = readParams(paramFile,"units")
	picoutPath = path_process(picoutPath) ;处理路径中的大小写，斜杠反斜杠等问题
	picName = filename_process(picName) ;处理文件名中的大小写，斜杠反斜杠等问题
;***********************************************************
	;拼标题用
	forecastTimeArr = str_split(forecastTime,"/")
	year = tointeger(forecastTimeArr(0))
	mon = tointeger(forecastTimeArr(1))
	day = tointeger(forecastTimeArr(2))
	timeRangeArr = tointeger(str_split(timeRange,"-"))
	
	;取NC文件
	dataFile = "/nfsshare/cdbdata/data/airPollution/" + forecastTimeArr(0) + "/" + forecastTimeArr(1) + "/" + forecastTimeArr(2) + "/"
	if (isfilepresent(dataFile + var + ".nc"))
		f = addfile(dataFile + var + ".nc", "r")
	else
		myPrint("No Data : Forecast Data is not Exist !")
		exit
	end if
	
	;根据时间尺度取数据范围
	if(timeType.eq."day")then
		startIndex = timeRangeArr(0)-1
		endIndex = timeRangeArr(1)-1
	end if
	
	if(timeType.eq."five")then
		mondays1 = days_in_month(year,mon)
		if(mon.eq.12)then
			mondays2 = days_in_month(year+1,1)
		else
			mondays2 = days_in_month(year,mon+1)
		end if
		if(day.ge.26)then
			leftday = mondays1-day
			startIndex = timeRangeArr(0)*5-5+leftday
			if(timeRangeArr(1).eq.6)then
				endIndex = mondays2 + leftday - 1
			else
				endIndex = timeRangeArr(1)*5-1+leftday
			end if
		end if
		if(day.lt.26)then
			numfive = toint((day-1)/5) + 1
			leftday = 4 - mod(day-1,5)
			if((numfive+timeRangeArr(1)).lt.6)then
				startIndex = timeRangeArr(0)*5 - 5 + leftday
				endIndex = timeRangeArr(1)*5 - 1 + leftday
			end if
			if((numfive+timeRangeArr(1)).eq.6)then
				startIndex = timeRangeArr(0)*5 - 5 + leftday
				endIndex = mondays1 - day - 1
			end if
			if((numfive+timeRangeArr(1)).gt.6 .and. (numfive+timeRangeArr(0)).le.6)then
				startIndex = timeRangeArr(0)*5 - 5 + leftday
				endIndex = timeRangeArr(1)*5 - 1 + leftday + mondays1 - 30
			end if	
			if((numfive+timeRangeArr(1)).gt.6 .and. (numfive+timeRangeArr(0)).gt.6)then
				startIndex = timeRangeArr(0)*5 - 5 + leftday  + mondays1 - 30
				endIndex = timeRangeArr(1)*5 - 1 + leftday + mondays1 - 30
			end if
		end if
	end if
	
	if(timeType.eq."week")then
		dayweeks = day_of_week(year,mon,day)
		if(dayweeks.ne.0)then
			startIndex = timeRangeArr(0)*7-7 + 7-dayweeks
			endIndex = timeRangeArr(1)*7-1 + 7-dayweeks
		else
			startIndex = timeRangeArr(0)*7-7
			endIndex = timeRangeArr(1)*7-1
		end if
	end if
	
	print(startIndex)
	print(endIndex)
	
	
	
	;根据变量判断是否取高度层数据
	if(var.eq."geopt" .or. var.eq."tk" .or. var.eq."rh")then
		lev = tointeger(height)
		data = f->$var$(startIndex:endIndex,{lev},:,:)
		datanew = dim_avg_n_Wrap(data,0)
	else
		;如果降水求和
		if(var.eq."prate")then
			data = f->$var$(startIndex:endIndex,:,:)
			datanew = dim_max_n_Wrap(data,0)
		;其他求平均
		else
			data = f->$var$(startIndex:endIndex,:,:)
			datanew = dim_avg_n_Wrap(data,0)
		end if
	end if
	

	;温度：绝对转摄氏
	if(var.eq."tk" .or. var.eq."t2")then
		datanew := datanew - 273.15
	end if
	
	;比湿，千克每千克 转 克每千克
	if(var.eq."q2")then
		datanew := datanew*1000
	end if
	
	olon = fspan(61.0,143.5,166)
	olat = fspan(14.0,57.5,88)
	olon!0          = "lon"
	olon@long_name  = "lon"
	olon@units      = "degrees_east"
	olon&lon        = olon
	olat!0          = "lat"
	olat@long_name  = "lat"
	olat@units      = "degrees_north"
	olat&lat        = olat
	
	;为二维数据定义经纬度信息
	datanew!1 = "lon"
	datanew!0 = "lat"
	datanew&lon = olon
	datanew&lat = olat
	
	;相对湿度和温度在高度层上对青藏高原等高海拔地区的缺测数据处理
	if(isStrSubset(picName,"RH") .or. isStrSubset(picName,"TK"))
		;将缺测值赋值为-99999.0,绘图时绘制为灰色
		datanew = where(ismissing(datanew),-99999.0,datanew)
	end if
	printVarSummary(datanew)
	;print(datanew({33},{90}))
	;绘图大小
	size = "930x930"	 
;****************************************************************************** 
	if(var.eq."aspc")then
		units = "吨/天/KM²"
	end if
	if(var.eq."mixh")then
		units = "米"
	end if
	if(var.eq."q2")then
		units = "g/kg"
	end if
	if(var.eq."prate")then
		units = "毫米"
	end if
	if(var.eq."hfx")then
		units = "W/㎡"
	end if
	if(var.eq."rh")then
		units = "%"
	end if
	if(var.eq."tk" .or. var.eq."t2")then
		units = "℃"
	end if
	;绘图，参数二维数据，色例文件，图片大小，输出路径，输出名称。返回图例个数
	nboxes = draw_chpic(datanew,colorcfg,size,picoutPath,picName)
	
	;加载字体
	fontfile="/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/font/msyh.ttc"
	fontsize= "15"
	fontsize2= "12"
	ws = 61.15
	hs = 696-0.022*0.868*(tointeger(nboxes)+3-(tointeger(nboxes)-5)/2.8)*696-10+tofloat(fontsize)+30-(tointeger(nboxes)-5)/0.8+41
	w1=ws-tofloat(fontsize)
	w2=ws-(4+strlen(units)/3)*tofloat(fontsize2)/2
	h1=hs
	h2=hs+tofloat(fontsize2)+5
	location2="+" + w1 + "+" + h1
	location3="+" + w2 + "+" + h2
	
	;在图例框中加图例两字
	AddChar(picoutPath,picName+".png",fontfile,location2,fontsize,"图例")
	;在图例框中加单位信息
	AddChar(picoutPath,picName+".png",fontfile,location3,fontsize2,"单位（" + units + "）")
	
	;加两个logo
	img1 = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/NCC.png"
    img2 = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/BCC.png"

    cmd1="convert "+picoutPath+picName+".png"+" -compose over "+img1+" -geometry 70x40+40+40 -composite "+picoutPath+picName+".png"
    system(cmd1)
    cmd2="convert "+picoutPath+picName+".png"+" -compose over "+img2+" -geometry 40x40+120+40 -composite "+picoutPath+picName+".png"
    system(cmd2)	
end 
exit
