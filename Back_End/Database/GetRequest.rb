#!/usr/bin/ruby -w
BEGIN{
	print <<"EOF"
Start
EOF
require 'logger'
file=File.open('log.txt',"w")
$log=Logger.new(file)
$log.level=Logger::INFO
$log.info "Test begins"
}
#Test begins


END{
	print <<"EOF"
End
EOF
$log.info "Test ends"
}
#Test ends


class Request
	
	@@select="Select "
	@@from=" from " 
	@@where=" where " 
	@@brand=" brand= "
	@@type=" Type= "
	@@sizing=" Sizing(having)="
	@@gender=" Gender="
	#separate mysql query into 3parts
	def initialize(knownBrand=nil,type=nil,gender=nil,searchSize=nil,searchBrand=nil) #initialize a query. Except for type and type
	    @knownBrand=knownBrand
	    @searchBrand=searchBrand
	    @type=type
	    @gender=gender
	    @searchSize=searchSize
	end
	def getGeneralSize() #get the query for actual size
		a=0
		result=''
		result+= @@select + 'actual_height' + @@from + 'primary' + @@where
            if @knownBrand!=nil
		result+=  @@brand + @knownBrand
		a=1  
	    end
	    if  @searchSize!=nil
		if a==1
		result+= ' and '
		end
		result+=  @@sizing + @searchSize
		a=1
	    end
	    if @gender!=nil
		if a==1
		result+= ' and '
		end
		result+=   @@gender + @gender
		a=1
	    end
	    if @type!=nil
		if a==1
		result+= ' and '
		end
		result+=   @@type + @type
	    end
	    $log.info result
	    return result
	end


	def getSpecialSize(actual_height) #get the query for special brand sie
	    result=''

	    result+= @@select + 'brand_size' + @@from
	    result+= @type + @gender
	    result+= @@where
            if @searchBrand!=nil
	        result+= @@brand + @searchBrand + ' and ' + @@sizing + String(actual_height)
	    	
	    end
	    result+= @@sizing + String(actual_height)
	    return result
	end
	
	    
end

while TRUE #main loop, type end to end


	puts "Known Brand(optional)"+' Type END to exit'
	knownBrand=gets.chomp
	if knownBrand.empty? 
	   knownBrand=nil
	end
	if knownBrand=='END'
 	break
	end

	puts "Search Brand(optional)"+' Type END to exit'
	searchBrand=gets.chomp
	if searchBrand.empty? 
	    searchBrand=nil
	end 
	if searchBrand=='END'
	break
	end


	puts "Type(necessary)"+' Type END to exit'
	type=gets.chomp	
	if type=='END'
	break
	end


	puts "Gender(necessary)"+' Type END to exit'
	gender=gets.chomp
	if gender=='END'
	break
	end
	
	puts "Known Size(optional)"+' Type END to exit'
	searchSize=gets.chomp
	if searchSize.empty? 
	    searchSize=nil	
	end
	if searchSize=='END'
	break	
	end
	if type.empty? or gender.empty?
	puts "Type/gender is invalid"
	next
	end
	# type and gender are necessary. If anyone is empty, continue this loop


cust1=Request.new(knownBrand = knownBrand,type = type,gender = gender,searchSize = searchSize,searchBrand = searchBrand)
result1 = cust1.getGeneralSize() #result1 to query the actual_size from PRIMARY
puts result1
result2 = cust1.getSpecialSize(10) #assume actual_size is 10
puts result2 #result2 to query the brand size according to actual_size
end	

