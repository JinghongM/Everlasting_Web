#!/usr/bin/ruby -w
load 'GetRequest.rb'
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
result1 = cust1.getBrandSize() 
puts result1

END{
	print <<"EOF"
End
EOF
$log.info "Test ends"
}
#Test ends
