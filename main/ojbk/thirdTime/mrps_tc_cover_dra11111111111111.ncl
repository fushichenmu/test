;******************************************
;author:JiangPeng
;create date：2017-10
;(色斑图)
;******************************************
load "$NCLJOB_ROOTS/extComponent/ncl_component/util/tools.ncl"
;******************************************
;******************************************
undef ("setCommonRes")
procedure setCommonRes(res)
begin
	res@gsnFrame                  = False
	res@gsnDraw                   = False
	; 最大化 默认为False，如果是True的话，NDC的XY会自动缩小0.02
	; res@gsnMaximize               = False
	; 图片右下角的说明文字“CONTOUR FROM 8 TO 56 BY 4”
	res@tiMainOn             	  = False    								;不开主标题
	res@gsnLeftString		 	  = "" 		   								;不开左标题
	res@gsnRightString		 	  = "" 		   								;不开右标题
	res@tmXBMinorOn			      = False 								;不打开副刻度
	res@tmYLMinorOn       		  = False 								;不打开副刻度
	; 左上角坐标
	res@vpXF                      = 0   
	res@vpYF                      = 1     
	; 调节矩形的长宽
	res@vpWidthF                  = 1.
	res@vpHeightF                 = 1.
	; 无数据时不显示任何文字
	res@cnConstFEnableFill		 = False
	res@cnNoDataLabelOn           = False
	res@cnConstFLabelOn           = False
	res@lbLabelBarOn 		   = False      ;颜色标签
	res@cnInfoLabelOn		   = False 		;不显示信息标签
	res@tmXBOn                   = False
	res@tmXTOn                   = False
	res@tmYLOn                   = False
	res@tmYROn                   = False
	res@tmXBMinorOn				= False 								;不打开副刻度
	res@tmYLMinorOn       	   	= False 								;不打开副刻度
end
;******************************************
;绘制色斑图
undef("drawContour")
function drawContour(data,lon,lat,areaName, configPath, outputName, outputPath,busid,elementType,dataInfoName,acc,paramsPath)
; 绘图数据，绘图经度范围，绘图纬度范围，区域名称（CH特殊处理），配置文件路径，输出文件名，输出路径，业务id，业务id预留字段，图例存放文件名，相关系数检验阈值，参数文件路径+名称）
begin
	minLon = min(lon)      
	maxLon = max(lon)
	minLat = min(lat)
	maxLat = max(lat)
	imgSizes = tointeger(str_split(readBusiINI(configPath, "imgSize_"+busid),","))   ;出图分辨率  
	wks_type = "png"  ;图片格式
	wks_type@wkWidth = imgSizes(0)
	wks_type@wkHeight = imgSizes(0)           ;长宽相等，正方形
	checkOrCreateDir(outputPath)   ;出图路径，若不存在则创建文件夹
	drawData = data 
	;颜色
	colorcfg = "$NCLJOB_ROOTS/extComponent/ncl_component/config/" + readBusiINI(configPath, "COLORCFG_"+busid+"_"+elementType)  ;出图的色例文件的相对路径及文件名
	cmap = getColorMap(colorcfg)   ;读取色例信息
	wks = gsn_open_wks(wks_type, outputPath + outputName) ;创建工作空间
	setvalues NhlGetWorkspaceObjectId()   ;获取工作空间对象，调整内存大小
		"wsMaximumSize" : 300000000
	end setvalues
	gsn_define_colormap(wks, cmap)  ;定义工作空间的颜色配置
	
	; 图例信息落文件（给后台java生成图例，合成图片使用）
	f = asciiread(colorcfg,-1,"string")  
	vs = str_split(f(4),",")
	vs = vs(::-1)
	rgb = f(11:)
	rgb = rgb(::-1)
	colorInfo = array_append_record("COLORVALUE="+str_join(vs,","),"RGB="+str_join(rgb,";"),0)
	delete([/vs,rgb/])
	if(isfilepresent(outputPath+ dataInfoName))then
		dataInfoArr = asciiread(outputPath+ dataInfoName,-1,"string")
		index = str_match_ind(dataInfoArr,"COLORVALUE=")
		if(.not.ismissing(index))then
			dataInfoArr(index:index+1) = colorInfo
		else
			dataInfoArr := array_append_record(dataInfoArr,colorInfo,0)
		end if
	else
		dataInfoArr = colorInfo
	end if
	asciiwrite(outputPath + dataInfoName,dataInfoArr)	
	
	
	
	
	cnLinesOn = readBusiINI(configPath, "cnLinesOn_"+busid)        ;是否绘制等值线
	cnFillOn = readBusiINI(configPath, "cnFillOn_"+busid)           ;是否绘制色斑
	XYon = readBusiINI(configPath,"isXYon_"+busid)            ;是否添加经纬框
	borderOn = readBusiINI(configPath,"borderOn_"+busid)   ;是否去除边框 默认保留
	mpGeoOn = readBusiINI(configPath,"mpGeoOn_"+busid)   ;是否添加地理信息图层（疑似已废，直接使用颜色，粗细绘制） 
	lambertOn = readBusiINI(configPath,"lambertOn_"+busid)   ;投影方式，默认等经纬，兰伯特投影才需要设置为True
	markerOn = readBusiINI(configPath,"cnMarkerOn_"+busid)   ;是否打点,相关系数检验

	res                        = True ;创建绘图参数
	setCommonRes(res)                 ;设置通用的绘图参数
	res@gsnAddCyclic            = False ;是否全球循环，全球为True
	res@mpMinLonF   			= minLon 
	res@mpMaxLonF    			= maxLon
	res@mpMinLatF    			= minLat
	res@mpMaxLatF   			= maxLat
	res@mpCenterLonF 			= (minLon+maxLon)*0.5 ;中心经度，中央子午线
	res@mpGridAndLimbOn      	= False ;是否绘制经纬度网格
	res@mpFillOn				= False ;是否显示地图填充
	res@cnLevels               = getColorValueDef(colorcfg) ;绘制等值线的值
	if(readParams(paramsPath,"cnLevels").ne."")then		;读取参数配置文件，如果有cnLevels，则替换colorcfg中的默认配置
		res@cnLevels := tofloat(str_split(readParams(paramsPath,"cnLevels"),","))
	end if
	res@cnLevelSelectionMode   = "ExplicitLevels" 选择绘制等值线的值为指定值
	if(XYon.eq."True")then
		;读取参数文件的配置信息
		tmXBLabelFontHeightF = readBusiINI(configPath, "X_LABEL_"+busid) ;X轴标签字体大小
		tmXBMajorLengthF = readBusiINI(configPath, "X_LENGTH_"+busid) ;X轴主刻度线长度
		tmXBMajorThicknessF = readBusiINI(configPath, "X_THICK_"+busid) ;X轴主刻度线宽
		tmXBTickSpacingF = readBusiINI(configPath, "X_SPACE_"+busid) ;X轴主刻度间隔
		tmYLTickSpacingF = readBusiINI(configPath, "Y_SPACE_"+busid)
		tmYLLabelFontHeightF = readBusiINI(configPath, "Y_LABEL_"+busid)
		tmYLMajorLengthF = readBusiINI(configPath, "Y_LENGTH_"+busid)
		tmYLMajorThicknessF = readBusiINI(configPath, "Y_THICK_"+busid)
		tmXMajorGrid = readBusiINI(configPath, "tmXMajorGrid_"+busid) ;是否绘制X坐标轴主刻度网格线
		tmXMajorGridLineDashPattern = tofloat(readBusiINI(configPath, "tmXMajorGridLineDashPattern_"+busid)) ;X坐标轴主刻度网格线线型
		tmXMajorGridThicknessF = tofloat(readBusiINI(configPath, "tmXMajorGridThicknessF_"+busid)) ;X坐标轴主刻度网格线线宽
		tmYMajorGrid = readBusiINI(configPath, "tmYMajorGrid_"+busid)
		tmYMajorGridLineDashPattern = tofloat(readBusiINI(configPath, "tmYMajorGridLineDashPattern_"+busid))
		tmYMajorGridThicknessF = tofloat(readBusiINI(configPath, "tmYMajorGridThicknessF_"+busid))	
		;底图属性	
		res@tmXBMode            	= "Explicit" 									;按给定的间隔绘制X轴主刻度
		res@tmXBTickSpacingF     	= tofloat(tmXBTickSpacingF)  					;主刻度间隔
		res@tmYLTickSpacingF     	= tofloat(tmYLTickSpacingF)
		;画坐标轴
		res@gsnMaximize  = True ;是否占满整个画布
		res@tmXBOn                   = True ;x轴的底部刻度线
		res@tmYLOn                   = True ;y轴的左边刻度线
		res@tmXBLabelFontHeightF	= tofloat(tmXBLabelFontHeightF) 				;X轴标签字体大小
		res@tmXBMajorLengthF		= tofloat(tmXBMajorLengthF)  					;设置X轴刻度长度
		res@tmXBMajorThicknessF		= tofloat(tmXBMajorThicknessF)					;x轴刻度厚度
		res@tmYLLabelFontHeightF	= tofloat(tmYLLabelFontHeightF)					;Y轴左坐标轴刻度字体大小
		res@tmYLMajorLengthF		= tofloat(tmYLMajorLengthF) 				;Y轴主刻度线长度
		res@tmYLMajorThicknessF 	= tofloat(tmYLMajorThicknessF)
		;坐标轴网格线
		res@tmXMajorGrid            = tmXMajorGrid   					;X轴显示网格线
		res@tmXMajorGridLineDashPattern = tmXMajorGridLineDashPattern  					;网格线为虚线
		res@tmXMajorGridThicknessF	= tmXMajorGridThicknessF   						;X轴主刻度网线粗细
		res@tmYMajorGrid            = tmYMajorGrid  					;Y轴显示网格线
		res@tmYMajorGridLineDashPattern = tmYMajorGridLineDashPattern  					;网格线为虚线
		res@tmYMajorGridThicknessF	= tmYMajorGridThicknessF    ;Y轴网线粗细
	else
		res@gsnMaximize               = False
		if(borderOn.eq."False")then
			; 去掉四周边框
			res@tmXBBorderOn          = False
			res@tmXTBorderOn          = False
			res@tmYLBorderOn          = False
			res@tmYRBorderOn          = False
		end if
	end if
	if(lambertOn.eq."True")then
		delete(res@mpCenterLonF) ;通过mpLambertMeridianF进行设置
		res@gsnDraw					= False ;关掉gsn绘图
		res@gsnFrame				= False ;关掉gsn绘图框架
		res@gsnAddCyclic            = False
		
		;底图属性
		res@mpFillOn				= False 
		res@mpGridAndLimbOn      	= False
		res@mpPerimOn 				   = False ;是否绘制地图边线
		res@mpOutlineDrawOrder      =  "PreDraw" ;在标准绘制前绘制边线
		res@mpProjection = "LambertConformal" ;"LambertEqualArea" 定义投影
		res@mpLambertMeridianF = 105.0 ;中央子午线，中心经度
		res@mpLimitMode = "LatLon" ;按给定经纬度范围绘制
		res@mpLambertParallel1F = 25     ;Default: .001 第一标准纬度
		res@mpLambertParallel2F = 47   ;Default: 89.999 第二标准纬度
		res@mpGridLineDashPattern= 5  ;绘制经纬度网格的虚线线型
		res@mpGridLineThicknessF = 0.5  ;绘制经纬度网格的虚线线宽
		res@mpNationalLineColor 	= "transparent" ;国界颜色
		res@mpGeophysicalLineColor	= "transparent" ;其他边线线颜色
		res@mpUSStateLineColor 		= "transparent" ;美国州界，中国省界
		res@gsnMaximize               = False
		res@tiMainOn                  = False ;是否显示主标题
		res@lbLabelBarOn 		      = False ;是否绘制色例
		if(areaName.eq."CH")then  ;若是绘制中国区域，则设置为固定经纬度范围
			res@mpMinLonF   			= 78.
			res@mpMaxLonF    			= 130.
			res@mpMinLatF    			= 15.
			res@mpMaxLatF   			= 56.
		end if
		if(busid.eq."MRPS-MODES-JYGWMS-CH-Q001".or.busid.eq."MRPS-MODES-JYGWMS-CH-Q002")then
			delete([/res@mpMinLonF,res@mpMaxLonF,res@mpMinLatF,res@mpMaxLatF/])
			res@mpLeftCornerLatF			= minLat							;左下角纬度
			res@mpRightCornerLatF 		    = maxLat							;右上角纬度
			res@mpLeftCornerLonF			= minLon					  	    ;左下角经度
			res@mpRightCornerLonF			= maxLon                            ;左下角经度
			res@mpLimitMode                 = "Corners"  ;采用Corners方式绘图，其余按照latlon方式绘图
		end if 
		 ;去掉四周边框
		res@tmXBBorderOn              = False
		res@tmXTBorderOn              = False
		res@tmYLBorderOn              = False
		res@tmYRBorderOn              = False
		;去掉刻度
		res@tmXBOn                    = False
		res@tmXTOn                    = False
		res@tmYLOn                    = False
		res@tmYROn                    = False
		;左上角坐标
		res@vpXF                      = 0     ;左上点离左边画布边缘的距离，设置为0时距离为0
		res@vpYF                      = 1     ;左上点离上边画布边缘的距离，设置为1时距离为0
		;调节画布的长宽
		res@vpWidthF                  = 1.   
		res@vpHeightF                 = 1.
		res@cnSmoothingOn           = True       ;设置等值线平滑，三次样条平滑
		res@cnSmoothingDistanceF    = 0.0001	 ;平滑系数，值越接近0越平滑
		; res@cnSmoothingTensionF    = 3			;使平滑的曲线不相交
	end if
	res@cnFillOn			   = cnFillOn		;是否填色
	if(cnFillOn.eq."True")then
		res@cnFillColors           = getColorOrder(colorcfg) 
	end if
	res@cnLineLabelsOn = False     ; 等值线标签默认关闭
	res@cnLinesOn              = cnLinesOn		;等值线是否显示
	
	if(cnLinesOn.eq."True")then   ;是否绘制等值线
		cnLineLabelsOn = readBusiINI(configPath, "cnLineLabelsOn_"+busid) ;打开等值线时，是否显示标签
		LineColor	= readBusiINI(configPath, "LineColor_"+busid)  ;等值线颜色
		cnLineThicknessF = tofloat(readBusiINI(configPath,"LineThick_"+busid))  ;设置等值线线宽
		cnLineLabelDensityF = tofloat(readBusiINI(configPath, "CL_DENSITY_"+busid))	 ;标签间隔
		cnLineLabelFontHeightF = tofloat(readBusiINI(configPath,"CL_LABEL_"+busid))   ;标签数值字体大小
		cnSmoothingDistanceF = tofloat(readBusiINI(configPath, "CS_DistanceF_"+busid));等值线平滑系数
		res@cnLineLabelsOn		   := cnLineLabelsOn		;等值线上的数字标签是否显示		
		res@gsnContourNegLineDashPattern = 5            ;设置小于0的等值线线型，此处是5号虚线
		if(readBusiINI(configPath,"ZEROLINE_"+busid).ne."")then   ;0线特殊处理，此处为加粗
			res@gsnContourZeroLineThicknessF = tofloat(readBusiINI(configPath,"ZEROLINE_"+busid))
		end if
		if(cnLineLabelsOn .eq."True") ;是否绘制等值线标签
			
			res@cnLineLabelBackgroundColor = "#FEFEFE" 		;标签底色为接近白色;若需要其他颜色或透明（-1）则另行配置		
			res@cnLineLabelDensityF       = tofloat(cnLineLabelDensityF)   	  ;标签间隔
			res@cnLineLabelInterval       = 1                  ;等值线标签间隔，设置1时，则每条线上都进行标签
			res@cnLineLabelFontHeightF     = cnLineLabelFontHeightF		;标签数值字体大小		
			res@cnLineLabelFormat		   = "@1.4f"       ;标签显示为小数点后一位
		end if
		res@cnLineColor			    = where(LineColor.eq."","black",LineColor)  ;等值线颜色
		res@cnLabelMasking            = True  				      ;等值线不穿过标签文字
		; res@cnSmoothingTensionF    	= 5			;使平滑的曲线不相交
		res@cnLineThicknessF		 = cnLineThicknessF		;等值线线宽
		res@cnSmoothingOn           = True       ;是否平滑
		res@cnSmoothingDistanceF    = 0.0001	
	end if
	mpLandFillColor = readBusiINI(configPath,"LandFillColor_"+busid)  ;陆地颜色
	if(mpLandFillColor.ne."")then
		res@mpFillOn = True
		res@mpLandFillColor = mpLandFillColor ;陆地颜色
	end if	
	mpGeophysicalLineColor = readBusiINI(configPath,"mpGeoLineColor_"+busid) 
	mpOutlineBoundary = readBusiINI(configPath,"mpOutlineBoundary_"+busid) ;是否添加地理边界（国界）
	res@mpGeophysicalLineColor = where(mpGeophysicalLineColor.eq."","transparent",mpGeophysicalLineColor);未设置颜色就默认透明
	res@mpUSStateLineColor 	 = "transparent"
	if(res@mpGeophysicalLineColor.ne."transparent")then
		mpGeophysicalLineThicknessF = tofloat(readBusiINI(configPath,"mpLineThicknessF_"+busid))	
		res@mpNationalLineThicknessF = 2.0	
		res@mpGeophysicalLineThicknessF = mpGeophysicalLineThicknessF
		if(mpOutlineBoundary.eq."")then
			res@mpOutlineBoundarySets  = "National"  ;添加国界线
		end if
		res@mpNationalLineColor    = mpGeophysicalLineColor
	end if
	plot = gsn_csm_contour_map(wks, drawData, res) ;绘制上面属性设置的图
	; 特殊等值线
	specialLine = readBusiINI(configPath,"specialLine_"+busid)   ;需要特殊处理的等值线值
	if(specialLine.ne."")then
		htres                           = True
		htres@gsnDraw				     = False
		htres@gsnFrame			         = False
		htres@gsnLeftString		     = "" 			;左上角不显示标签
		htres@gsnCenterString		     = "" 			;左上角不显示标签
		htres@gsnRightString		     = "" 			;右上角不显示标签
		htres@cnFillOn                   = False
		htres@cnLineLabelsOn             = True
		htres@cnInfoLabelOn		      = False
		htres@cnLineColor                = readBusiINI(configPath,"specialLineColor_"+busid)		;等值线颜色
		htres@cnLabelMasking             = True   		;等值线不穿过文字
		htres@cnLinesOn                  = True   		;等值线数据是否显示
		htres@cnLineLabelBackgroundColor  = "white"
		htres@cnLevelSelectionMode        = "ExplicitLevels"       ; set explicit contour levels
		htres@cnLevels                    = tofloat(str_split(specialLine,","))
		htres@cnLineThicknessF            = tofloat(readBusiINI(configPath,"specialLineThickness_"+busid))  		;等值线粗细
		htres@cnLineLabelFontHeightF      = 0.008
		htres@cnSmoothingOn		       = True
		htres@cnSmoothingDistanceF        = 0.001
		htres@cnLineLabelFormat		   = "@1.4f"	
		line = gsn_csm_contour(wks, drawData, htres)		
		overlay(plot,line)
	end if
	if(markerOn.eq."True")then                ;打点，相关系数检验
		number = tofloat(acc)
		; 打点
		mksres               		    = True    	;marker属性
		mksres@gsMarkerIndex		    = 16     	;空心圆点4,实心点16
		mksres@gsMarkerColor 		    = "black"						
		mksres@gsMarkerSizeF 		    = 2.5
		size = dimsizes(drawData)
		zlon = drawData&lon
		zlat = drawData&lat
		; 循环筛选出需要打点的经纬度
		do i = 0,size(0) - 1
			do j = 0,size(1) - 1
				if(.not.ismissing(drawData(i,j)) .and. abs(drawData(i,j)).ge. number)
					if(.not.isdefined("lats"))then
						lats = zlat(i)
						lons = zlon(j)
					else
						lats := array_append_record(lats,zlat(i),0)
						lons := array_append_record(lons,zlon(j),0)
					end if					
				end if
			end do
		end do
		mark = gsn_add_polymarker(wks, plot, lons, lats, mksres)   ;点直接打在plot上的
	end if
	draw(plot) ;绘制，一般是将所有的属性设置完以后进行绘图。
	frame(wks) ;释放工作空间
	transparentBkColor("white -crop "+(imgSizes(0)+"x"+imgSizes(1)+"+"+imgSizes(2)+"+"+imgSizes(3)), outputPath + outputName + ".png");调用imageMagic切图
	delete([/drawData,plot,wks,res,cmap/]) ;释放资源
	return 0
end
;******************************************
;createImg 生成产品图片
;******************************************
undef ("createImg")
function createImg(filePath,configPath, params)
begin
	;参数文件路径
	paramsPath= filePath	
	if(.not.isfilepresent(filePath))then
		myPrint("No paramsPath : " + paramsPath)
		return -1
	end if
	
	;读取数据
	imgOutPutPath = readParams(paramFile,"imgOutPutPath")    ;出图路径
	imgOutPutPath = where(imgOutPutPath .eq. "",readParams(paramFile,"localFilePath"),imgOutPutPath)   ;出图路径为空，用localFilePath替换
	datapath = imgOutPutPath + readParams(paramFile, "imgDataName")	   ;画图数据路径
	busid = readParams(paramsPath,"busid")   ;业务id
	resVar = readParams(paramsPath,"resVar")   ; 数据要素名称
	elementType = readParams(paramsPath,"elementType")  ; 不定。本脚本用于相同业务id下不同的产品的图例的配置
	dataInfoName = readParams(paramsPath,"dataInfoName")   ; 原先存放数据缺测情况（数据完整性），此处用于添加后台绘制图例所需的信息
	if(.not.isfilepresent(datapath))then                 ;判断画图数据是否存在
		myPrint("No dataPath : " + datapath)
		exit
	end if
	fl = addfile(datapath, "r")   ;加载数据
	data  = fl->$resVar$		;读数据
	draLat = readParams(paramsPath,"draLat")  ;绘图纬度
	draLon = readParams(paramsPath,"draLon")  ;绘图经度
	draLat = where(draLat.eq."",readParams(paramsPath,"lat"),draLat)  ;若没传，就用取数据的经纬度
	draLon = where(draLon.eq."",readParams(paramsPath,"lon"),draLon)  ;若没传，就用取数据的经纬度
	lat = tofloat(str_split(draLat,","))   ;以逗号隔开的开始结束纬度，拆分为数组
	lon = tofloat(str_split(draLon,","))   ;
	if(all(ismissing(data))) then    ;数据全缺测就不画图
		myPrint("Data missing: Cannot create pic.")
		return -1
	end if
	imgName = readParams(paramsPath,"imgName")  ;生成图片文件的名称，不带后缀
	areaName = readParams(paramsPath,"areaName") ;区域名称，只在画中国(CH)时生效，绘图经纬度范围固定
	if(readBusiINI(configPath,"DataReset_"+busid).eq."True")then ;字段“DataReset_”用于判断是否需要对绘图数据进行插值
		olat = fspan(min(lat),max(lat),tointeger((max(lat)-min(lat))/0.2)+1)  ;按照设置间隔（0.2）以及最大最小值，生成等间隔序列
		olon = fspan(min(lon),max(lon),tointeger((max(lon)-min(lon))/0.2)+1)  
		olon!0          = "lon"    ;对数组0维赋名称    
		olon@long_name  = "lon"   ;给数组赋名称
		olon@units      = "degrees-east"  ;给数组赋单位
		olon&lon        = olon  ;给数组0维赋地理坐标
		olat!0          = "lat"
		olat@long_name  = "lat"
		olat@units      = "degrees_north"
		olat&lat        = olat
		tmp1 = linint2_Wrap(data&lon,data&lat,data,True,olon,olat,0) ;双线性插值（格点-格点），（要插值的格点数据的经度，要插值的格点数据的纬度，插值数据，插值以后的经度数组，插值以后的纬度数组，保留关键字）
		data := smth9_Wrap(tmp1, 0.50, 0.25, False)		;9点平滑
		data = smth9_Wrap(data, 0.50, 0.25, False)
	end if
	acc = readParams(paramsPath,"acc")   ;用于信度检验打点的阈值
	result = drawContour(data,lon,lat,areaName,configPath, imgName, imgOutPutPath,busid,elementType,dataInfoName,acc,paramsPath)
	return 1
end

;******************************************
begin
    ;判断paramFile变量是否存在
	if(.not.isvar("paramFile"))then
		paramFile="null"
		myPrint("echo param is null")
		exit
	end if 
		;判断参数路径是否存在
	if(.not.isfilepresent(paramFile))then
		myPrint("No params:" + paramFile)
		return -1
	end if 	
	configPath = "$NCLJOB_ROOTS/extComponent/ncl_component/business/dra/forecast/station/pb/mrps_tc_cover/mrps_tc_cover_dra.config"
    rtn = createImg(paramFile, configPath,"")
end
exit