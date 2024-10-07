/*
 * searchTermsHighlight 1.1 - jQuery plugin to highlight search terms used to find a site.
 * http://www.alexanderdickson.com/projects/jquery-plugins/searchtermshighlight
 *
 *
 * Copyright (c) 2009 Alex Dickson
 * Licensed under the MIT licenses.
 * See website for more info.
 *
 */

(function($){  
  $.fn.searchTermsHighlight = function(options) {   
    
    if (typeof options === 'object') {

        var defaults = {
    		displayText: 'It looks like you searched {SEARCH_ENGINE} to get here. The following terms have been automatically highlighted: {SEARCH_TERMS}.',
            maxTerms: 5,
            termClass: 'search-term',
            termClassPrefix: 'term-',
            textPlacement: function(text, contentArea) {
                contentArea.before('<p>' + text + '</p>');
            },
            debugTerms: false
            
            
    	};	
    	var options = $.extend(defaults, options);   
    
    };
    
    var self = this;
    
    // Terms used in the referrer
    var terms = [];
    // The classes for the terms
    var termsClasses = {};
    // The search engine found in the referrer
    var searchEngine;
    
    var init = function() {
        
        if (options === 'toggle'){ toggleTermHighlighting(); return this; }

        
        if (options.debugTerms) {
            searchEngine = 'DebugMode';
            terms = options.debugTerms;
        } else {
            var referrer = document.referrer;
            
            if ( ! referrer) {
                return this;
            };
               
            // Get the parts we want from the referrer
            var referrerParts = referrer.split(/https?:\/\/(.+)\//);
            var domain = referrerParts[1];
            var queryString = referrerParts[2];
            
            
            // Turn it into a useful array
            var queryParams = {};
            
            $.each(queryString.split(/&/), function(i, part){
                var queryParamParts = part.split('=');
                queryParams[queryParamParts[0]] = queryParamParts[1];
            });
            
            
            // Which search engine did they use? Is it supported?    
            var searchQuery = '';
            
            // Which search engine are we using? Check Google first because it is most popular
            if (domain.match(/google.com/)) {
                searchEngine = 'Google';
                searchQuery = queryParams['q'];
            }
            else if (domain.match(/yahoo.com/)) {
                searchEngine = 'Yahoo';
                searchQuery = queryParams['p'];
            }
            else if (domain.match(/bing.com/)) {
                searchEngine = 'Bing';
                searchQuery = queryParams['q'];
			
			}
			else if (domain.match(/localhost:8000/)) {
                searchEngine = 'GG';
                searchQuery = queryParams['searchVal'];
                
            } else {
                // This search engine isn't supported so we'll just bail out
                return this;
            };
            
            terms = searchQuery.split('+');
        };
        
        terms = terms.splice(0, options.maxTerms);
        
        var termsPretty = '';
        $.each(terms, function(i, term){
            
            // Normalise term
            
            var normalisedTerm = term.toLowerCase();
            
            // Create regex and replace string
            termsClasses[normalisedTerm] = [options.termClass, options.termClassPrefix + i];
            
            // Create a pretty readable string
            var prettyReplace = '<span class="' + termsClasses[normalisedTerm].join(' ')  + ' list-words">' + term + '</span>';
            
            if (terms.length == 1) {
                termsPretty = prettyReplace;
            } else if (i != terms.length - 1) {
                termsPretty += prettyReplace + ', ';
            } else {
                termsPretty = termsPretty.substr(0, termsPretty.length - 2);
                termsPretty += ' and ' + prettyReplace;
            };
            
                
        });
        
           
        var text = options.displayText.replace(/{SEARCH_ENGINE}/, searchEngine).replace(/{SEARCH_TERMS}/, termsPretty);
        
        
        if (typeof options.textPlacement == 'function') {
              options.textPlacement(self, text);
        };
        
        // Add the highlighting
        addTermHighlighting();
      
    };
    
    
    var toggleTermHighlighting = function() {
        var $highlightedTerms = self.find('span.terms-matched');
        
        if ($highlightedTerms.length) {
           
           $highlightedTerms.each(function() {
              
              var node = $(this).html();
           
               $(this).before(node);
               
               $(this).remove();
               
           });
            
                     
        } else {

            addTermHighlighting();
        } 
        
    };
    
    var addTermHighlighting = function() {
        

        var regex = new RegExp('(\\b(' + terms.join('|') + ')\\b)', 'gmi')
         
         return self.each(function() {  
    	   var obj = $(this);
           
           
           findText(obj[0], regex, function(node, match) {
                var span = document.createElement('span');
                
                span.className = termsClasses[match[0].toLowerCase()].join(' ') + ' terms-matched';
                node.splitText(match.index+match[0].length);
                span.appendChild(node.splitText(match.index));
                node.parentNode.insertBefore(span, node.nextSibling);
            });

           
    	 });
        
    };
    
    // Utility functions
    
    // findText - Thanks Bobince http://stackoverflow.com/questions/1501007/#1501213
    var findText = function(element, pattern, callback) {
        for (var childi= element.childNodes.length; childi-->0;) {
            var child= element.childNodes[childi];
            if (child.nodeType==1) {
                findText(child, pattern, callback);
            } else if (child.nodeType==3) {
                var matches= [];
                var match;
                while (match= pattern.exec(child.data))
                    matches.push(match);
                for (var i= matches.length; i-->0;)
                    callback.call(window, child, matches[i]);
            }
        }
    }

    
    init();

   
    
  };  
 })(jQuery); 
 