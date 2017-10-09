#!/usr/bin/ruby -w
require 'logger'

class Request
	
	@@select="Select "
	@@from=" from " 
	@@where=" where " 
	@@brand="brand= "
	@@type="Type= "
	@@sizing="Sizing(having)="
	@@gender="Gender="
	#separate mysql query into 3parts
	def initialize(knownBrand=nil,type=nil,gender=nil,searchSize=nil,searchBrand=nil) #initialize a query. Except for type and type
	    @knownBrand=knownBrand
	    @searchBrand=searchBrand
	    @type=type
	    @gender=gender
	    @searchSize=searchSize
	    @typeTable=@gender+@type
	    setLogger()
	end
	def setLogger()
	    if File.exist? File.expand_path "./log.txt"
	    logFile = File.open('log.txt', 'a')
	    puts "txt exists"
	    else
	    logFile = File.open('log.txt','w')
	    puts "txt not exists, create a new log file instead"
	    end


	    log = Logger.new(logFile)
	    logInfo = "A request inputs:" 
	    if @knownBrand != nil 
	    logInfo += ' known Brand: ' + @knownBrand
	    end
	    if @searchBrand != nil
	    logInfo += ' search Brand: ' + @searchBrand
	    end	 

	    logInfo += ' search type: ' + @type + ' gender: ' + @gender 
	       
	    if @searchSize != nil
	    logInfo += ' search size: ' + @searchSize
	    end
	    log.info(logInfo)   
	    logFile.close()
	end
	
	def getBrandSize()
	    result=''#necessary
	    result += @@select + 'brand_size' + @@from + 'primary' + ' and ' + @typeTable #necessary
	    result += @@where + 'primary.actual_height=' + @typeTable + '.actual_height' #necessary
	    result += ' and ' + 'Primary.' + @@gender + @gender #necessary
	    result += ' and ' + 'Primary.' + @@type + @type #necessary
	    if @knownBrand != nil #optional
		result += ' and ' + 'Primary.' + @@brand + @knownBrand 
	    end
	    if @searchSize != nil #optional
	        result += ' and ' + 'Primary.' + @@sizing + @searchSize 
	    end

	    if @searchBrand != nil #optional
		result += ' and ' + @typeTable + '.' + @@brand + @searchBrand 
	    end
		
	    return result
	end
end

