```bash
ansible-aci-iac % ansible-playbook playbooks/config_apic.yaml --check          

PLAY [Deploy APIC configuration] **********************************************************************************************************************************************************************************************************************************************************

TASK [Inlcude present_apic_access_policies role] ******************************************************************************************************************************************************************************************************************************************

TASK [Inlcude process_data role] **********************************************************************************************************************************************************************************************************************************************************

TASK [process_data : Read all YAML files in the data_directory into apic_configuration] ***************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/tenant_PROD.yaml)
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/access_policies.yaml)

TASK [process_data : Read all YAML files in the previous_data_directory into previous_apic_configuration] *********************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [process_data : Set previous_apic_configuration as empty dict if no previous_data_directory] *****************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Include default variables] *******************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct current_extracted_data] ************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/vlan_pools)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/vlan_pools/ranges)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/physical_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/routed_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/interface_policies/cdp_policies)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/interface_policies/lldp_policies)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/interface_policies/link_level_policies)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/leaf_interface_policy_groups)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/aaeps)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/aaeps/physical_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/aaeps/routed_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/aaeps/endpoint_groups)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/leaf_interface_profiles)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/leaf_interface_profiles/selectors)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/leaf_interface_profiles/selectors/port_blocks)
ok: [fabric1_apic1 -> localhost] => (item=apic/access_policies/leaf_interface_profiles/selectors/sub_port_blocks)

TASK [process_data : Construct previous_extracted_data] ***********************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1] => (item=apic/access_policies/vlan_pools) 
skipping: [fabric1_apic1] => (item=apic/access_policies/vlan_pools/ranges) 
skipping: [fabric1_apic1] => (item=apic/access_policies/physical_domains) 
skipping: [fabric1_apic1] => (item=apic/access_policies/routed_domains) 
skipping: [fabric1_apic1] => (item=apic/access_policies/interface_policies/cdp_policies) 
skipping: [fabric1_apic1] => (item=apic/access_policies/interface_policies/lldp_policies) 
skipping: [fabric1_apic1] => (item=apic/access_policies/interface_policies/link_level_policies) 
skipping: [fabric1_apic1] => (item=apic/access_policies/leaf_interface_policy_groups) 
skipping: [fabric1_apic1] => (item=apic/access_policies/aaeps) 
skipping: [fabric1_apic1] => (item=apic/access_policies/aaeps/physical_domains) 
skipping: [fabric1_apic1] => (item=apic/access_policies/aaeps/routed_domains) 
skipping: [fabric1_apic1] => (item=apic/access_policies/aaeps/endpoint_groups) 
skipping: [fabric1_apic1] => (item=apic/access_policies/leaf_interface_profiles) 
skipping: [fabric1_apic1] => (item=apic/access_policies/leaf_interface_profiles/selectors) 
skipping: [fabric1_apic1] => (item=apic/access_policies/leaf_interface_profiles/selectors/port_blocks) 
skipping: [fabric1_apic1] => (item=apic/access_policies/leaf_interface_profiles/selectors/sub_port_blocks) 
skipping: [fabric1_apic1]

TASK [process_data : Construct present_extracted_data] ************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct absent_extracted_data] *************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [present_apic_access_policies : Create/Modify VLAN Pools] ****************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_vlan_pools_name': 'static', 'apic_access_policies_vlan_pools_allocation': 'static'})
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_vlan_pools_name': 'dynamic', 'apic_access_policies_vlan_pools_allocation': 'dynamic'})

TASK [present_apic_access_policies : Create/Modify VLAN Pools encap blocks] ***************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_vlan_pools_name': 'static', 'apic_access_policies_vlan_pools_allocation': 'static', 'apic_access_policies_vlan_pools_ranges_from': 201, 'apic_access_policies_vlan_pools_ranges_to': 299, 'apic_access_policies_vlan_pools_ranges_allocation': 'inherit', 'apic_access_policies_vlan_pools_ranges_role': 'external'})
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_vlan_pools_name': 'dynamic', 'apic_access_policies_vlan_pools_allocation': 'dynamic', 'apic_access_policies_vlan_pools_ranges_from': 1000, 'apic_access_policies_vlan_pools_ranges_to': 1099, 'apic_access_policies_vlan_pools_ranges_allocation': 'inherit', 'apic_access_policies_vlan_pools_ranges_role': 'external'})

TASK [present_apic_access_policies : Create/Modify Physical Domains] **********************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_physical_domains_name': 'phys', 'apic_access_policies_physical_domains_vlan_pool': 'static', 'apic_access_policies_physical_domains_allocation': 'static'})
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_physical_domains_name': 'phys-nh1-mappings', 'apic_access_policies_physical_domains_vlan_pool': 'static', 'apic_access_policies_physical_domains_allocation': 'static'})

TASK [present_apic_access_policies : Bind Physical Domain to VLAN Pools] ******************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_physical_domains_name': 'phys', 'apic_access_policies_physical_domains_vlan_pool': 'static', 'apic_access_policies_physical_domains_allocation': 'static'})
ok: [fabric1_apic1 -> localhost] => (item={'apic_access_policies_physical_domains_name': 'phys-nh1-mappings', 'apic_access_policies_physical_domains_vlan_pool': 'static', 'apic_access_policies_physical_domains_allocation': 'static'})

TASK [present_apic_access_policies : Create/Modify Routed Domains] ************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind Routed Domain to VLAN Pools] ********************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Policies CDP Interface Policies] ************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Policies LLDP Interface Policies] ***********************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Policies Link Level Interface Policies] *****************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Interface Policy Leaf Policy Groups] ********************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify AAEPs] *********************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind AEPs to Physical Domains] ***********************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind AEPs to Routed Domains] *************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind EPG to AEP] *************************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Interface Policy Leaf Profiles] *************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Interface Policy Leaf Profile Interface Selectors] ******************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Port Blocks of Access Interface Policy Leaf Profile Interface Selectors] ***************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Sub Port Blocks of Access Interface Policy Leaf Profile Interface Selectors] ***********************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [Inlcude present_apic_tenants role] **************************************************************************************************************************************************************************************************************************************************

TASK [Inlcude process_data role] **********************************************************************************************************************************************************************************************************************************************************

TASK [process_data : Read all YAML files in the data_directory into apic_configuration] ***************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/tenant_PROD.yaml)
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/access_policies.yaml)

TASK [process_data : Read all YAML files in the previous_data_directory into previous_apic_configuration] *********************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [process_data : Set previous_apic_configuration as empty dict if no previous_data_directory] *****************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Include default variables] *******************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct current_extracted_data] ************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/vrfs)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/bridge_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/bridge_domains/subnets)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles/endpoint_groups)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles/endpoint_groups/physical_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles/endpoint_groups/static_ports)

TASK [process_data : Construct previous_extracted_data] ***********************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1] => (item=apic/tenants) 
skipping: [fabric1_apic1] => (item=apic/tenants/vrfs) 
skipping: [fabric1_apic1] => (item=apic/tenants/bridge_domains) 
skipping: [fabric1_apic1] => (item=apic/tenants/bridge_domains/subnets) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles/endpoint_groups) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles/endpoint_groups/physical_domains) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles/endpoint_groups/static_ports) 
skipping: [fabric1_apic1]

TASK [process_data : Construct present_extracted_data] ************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct absent_extracted_data] *************************************************************************************************************************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [present_apic_tenants : Create/modify Tenants] ***************************************************************************************************************************************************************************************************************************************
changed: [fabric1_apic1 -> localhost] => (item={'apic_tenants_name': 'PROD'})
changed: [fabric1_apic1 -> localhost] => (item={'apic_tenants_name': 'PROD'})

TASK [present_apic_tenants : Create/Modify VRFs] ******************************************************************************************************************************************************************************************************************************************
changed: [fabric1_apic1 -> localhost] => (item={'apic_tenants_name': 'PROD', 'apic_tenants_vrfs_name': 'PROD', 'apic_tenants_vrfs_data_plane_learning': True, 'apic_tenants_vrfs_enforcement_direction': 'ingress', 'apic_tenants_vrfs_enforcement_preference': 'enforced', 'apic_tenants_vrfs_preferred_group': False})
changed: [fabric1_apic1 -> localhost] => (item={'apic_tenants_name': 'PROD', 'apic_tenants_vrfs_name': 'PROD', 'apic_tenants_vrfs_data_plane_learning': True, 'apic_tenants_vrfs_enforcement_direction': 'ingress', 'apic_tenants_vrfs_enforcement_preference': 'enforced', 'apic_tenants_vrfs_preferred_group': False})

TASK [present_apic_tenants : Create/Modify Bridge Domains] ********************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_tenants : Create/Modify Bridge Domains Subnets] ************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_tenants : Create/Modify Application Profiles] **************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_tenants : Create/Modify Endpoint Groups] *******************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_tenants : Bind EPGs to Physical Domains] *******************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_tenants : Bind Static paths to EPGs] ***********************************************************************************************************************************************************************************************************************************
skipping: [fabric1_apic1]

PLAY RECAP ********************************************************************************************************************************************************************************************************************************************************************************
fabric1_apic1              : ok=18   changed=2    unreachable=0    failed=0    skipped=25   rescued=0    ignored=0   

ansible-aci-iac % 
```