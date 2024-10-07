let $xml-test := <root>
                    <item id="1">Item1</item>
                </root>

return concat(name($xml-test//@id), "=",  data($xml-test//@id)) 

