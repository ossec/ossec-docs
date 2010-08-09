
.. object:: include 

    Load a single rule file.  

    **Allowes:** Path and file name of rule to load example: rules/config.xml 

        
.. object:: rule 

    
    Load a single rule file.  

    **Allowes:** Path and file name of rule to load example: rules/config.xml 

    .. note:: 

        This is the same as include, but created to keep the syntax constant with 
        other sections of the rules config. 

.. object:: rule_dir 

    Load a directory of rules.  The order of loaded files will be in alphebics order 
    and will not load any files that have been loaded before. 

    **Attributes:** 
    
    - *pattern*: is a regex match string use to detemine if a file needs to be 
      loaded. 
        
        - *Defaults*: regex "_rules.xml$" is used unless another one is specified. 
      
    **Allowes:** Path to a directoy of rule files 

    **Example:**

    #. Loading all rules in directory /var/ossec/rules ending ending with _rules.xml 
        
        .. code-block:: xml 
            
            <ossec_config>
                <rules>
                    <rules_dir>rules</rules_dir>
                </rules>
            </ossec_config>

    #. Loading all rules in directory /var/ossec/rules/plugins ending with .xml 

        .. code-block:: xml 
            
            <ossec_config>
                <rules>
                    <rules_dir pattern=".xml$">rules</rules_dir>
                </rules>
            </ossec_config>


