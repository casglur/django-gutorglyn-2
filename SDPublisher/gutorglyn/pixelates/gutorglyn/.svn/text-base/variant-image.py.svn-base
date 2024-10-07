"""Create your XML Element Processors here."""

import inspect


PIXELISE_PATTERNS = {
    'pb':'pb'    
}

def pb(element, context, args):
    
    imgIDFull = element.get_attribute_value('n')
    llgcRef = '_llgc_'
    
    try:
        lang = args['request'].COOKIES['gutorglynlang']
    except:
        lang = 'cy'        
           
    
    if imgIDFull == '':
        imgID = ''
        imgSrc = '/static/img/icons/manuscript-thumbnail_%s.png' % lang      
    
    if llgcRef not in imgIDFull:        
        imgID = imgIDFull
        imgRef = '['+imgID+']'
        imgSrc = '/static/img/icons/manuscript-thumbnail_%s.png' % lang    
        
        if context == "begin":        
            html = '<br/><img class="manuscript-image" src="%s"/>' % (imgSrc)
            return html
        
        if context == "end":              
            html='</a>&nbsp;&nbsp;%s<br/>'  % (imgRef)
            return html         
    else:  
                                
        imgID = imgIDFull.split('_')[2]
        imgRef = '[' + imgIDFull.split('_')[0] + ']'
    
        if imgID == '':
            imgLink = ''
        else:
            imgLink = 'http://dams.llgc.org.uk/behaviour/llgc-id:%s/fedora-bdef:image/reference' % imgID
        
        if imgID == '':            
            imgSrc = 'manuscript-thumbnail_%s.png' % lang
            imgThumbHtml = '<img class="manuscript-image" src="/static/img/icons/%s"/>' % imgSrc
        else:
            imgSrc = 'http://dams.llgc.org.uk/behaviour/llgc-id:%s/fedora-bdef:image/reference' % imgID
            imgThumbHtml = '<img src="%s"/>' % imgSrc
        
        if context == "begin":        
            html = '<a class="external-image-link" href="%s" target="_blank">%s</a><br/>%s' % (imgLink, imgRef,imgThumbHtml)
            return html
        
        if context=="end":              
            html=''
            return html           
    
    