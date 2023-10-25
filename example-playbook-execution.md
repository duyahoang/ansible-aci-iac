access_policies.yaml
```yaml
---
apic:
  access_policies:

    vlan_pools:
      - name: static
        allocation: static
        ranges:
          - from: 201
            to: 299
      - name: dynamic
        allocation: dynamic
        ranges:
          - from: 1000
            to: 1099

    physical_domains:
      - name: phys
        vlan_pool: static
      - name: phys-nh1-mappings
        vlan_pool: static
```

tenant_PROD.yaml
```yaml
apic:
  tenants:
    - name: PROD
      vrfs:
        - name: PROD
```
```bash
ansible-playbook playbooks/config_apic.yaml --check          

PLAY [Deploy APIC configuration] *********************************************************************************************************************************************

TASK [Inlcude present_apic_access_policies role] *****************************************************************************************************************************

TASK [Inlcude process_data role] *********************************************************************************************************************************************

TASK [process_data : Read all YAML files in the data_directory into apic_configuration] **************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/tenant_PROD.yaml)
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/tenant_nh1.yaml)
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/access_policies.yaml)

TASK [process_data : Read all YAML files in the previous_data_directory into previous_apic_configuration] ********************************************************************
skipping: [fabric1_apic1]

TASK [process_data : Set previous_apic_configuration as empty dict if no previous_data_directory] ****************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Include default variables] ******************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct current_extracted_data] ***********************************************************************************************************************
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

TASK [process_data : Construct previous_extracted_data] **********************************************************************************************************************
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

TASK [process_data : Construct present_extracted_data] ***********************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct absent_extracted_data] ************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [present_apic_access_policies : Create/Modify VLAN Pools] ***************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/vlan_pools/name': 'static', 'apic/access_policies/vlan_pools/allocation': 'static'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/vlan_pools/name': 'dynamic', 'apic/access_policies/vlan_pools/allocation': 'dynamic'})

TASK [present_apic_access_policies : Create/Modify VLAN Pools encap blocks] **************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/vlan_pools/name': 'static', 'apic/access_policies/vlan_pools/allocation': 'static', 'apic/access_policies/vlan_pools/ranges/from': 201, 'apic/access_policies/vlan_pools/ranges/to': 299, 'apic/access_policies/vlan_pools/ranges/allocation': 'inherit', 'apic/access_policies/vlan_pools/ranges/role': 'external'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/vlan_pools/name': 'dynamic', 'apic/access_policies/vlan_pools/allocation': 'dynamic', 'apic/access_policies/vlan_pools/ranges/from': 1000, 'apic/access_policies/vlan_pools/ranges/to': 1099, 'apic/access_policies/vlan_pools/ranges/allocation': 'inherit', 'apic/access_policies/vlan_pools/ranges/role': 'external'})

TASK [present_apic_access_policies : Create/Modify Physical Domains] *********************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/physical_domains/name': 'phys', 'apic/access_policies/physical_domains/vlan_pool': 'static', 'apic/access_policies/physical_domains/allocation': 'static'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/physical_domains/name': 'phys-nh1-mappings', 'apic/access_policies/physical_domains/vlan_pool': 'static', 'apic/access_policies/physical_domains/allocation': 'static'})

TASK [present_apic_access_policies : Bind Physical Domain to VLAN Pools] *****************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/physical_domains/name': 'phys', 'apic/access_policies/physical_domains/vlan_pool': 'static', 'apic/access_policies/physical_domains/allocation': 'static'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/access_policies/physical_domains/name': 'phys-nh1-mappings', 'apic/access_policies/physical_domains/vlan_pool': 'static', 'apic/access_policies/physical_domains/allocation': 'static'})

TASK [present_apic_access_policies : Create/Modify Routed Domains] ***********************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind Routed Domain to VLAN Pools] *******************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Policies CDP Interface Policies] ***********************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Policies LLDP Interface Policies] **********************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Policies Link Level Interface Policies] ****************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Interface Policy Leaf Policy Groups] *******************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify AAEPs] ********************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind AEPs to Physical Domains] **********************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind AEPs to Routed Domains] ************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Bind EPG to AEP] ************************************************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Interface Policy Leaf Profiles] ************************************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Access Interface Policy Leaf Profile Interface Selectors] *****************************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Port Blocks of Access Interface Policy Leaf Profile Interface Selectors] **************************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Create/Modify Sub Port Blocks of Access Interface Policy Leaf Profile Interface Selectors] **********************************************
skipping: [fabric1_apic1]

TASK [present_apic_access_policies : Clean up data] **************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [Inlcude present_apic_tenants role] *************************************************************************************************************************************

TASK [Inlcude process_data role] *********************************************************************************************************************************************

TASK [process_data : Read all YAML files in the data_directory into apic_configuration] **************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/tenant_PROD.yaml)
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/tenant_nh1.yaml)
ok: [fabric1_apic1 -> localhost] => (item=/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/data/fabric1/apic_configuration/access_policies.yaml)

TASK [process_data : Read all YAML files in the previous_data_directory into previous_apic_configuration] ********************************************************************
skipping: [fabric1_apic1]

TASK [process_data : Set previous_apic_configuration as empty dict if no previous_data_directory] ****************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Include default variables] ******************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct current_extracted_data] ***********************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/vrfs)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/bridge_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/bridge_domains/subnets)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles/endpoint_groups)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles/endpoint_groups/physical_domains)
ok: [fabric1_apic1 -> localhost] => (item=apic/tenants/application_profiles/endpoint_groups/static_ports)

TASK [process_data : Construct previous_extracted_data] **********************************************************************************************************************
skipping: [fabric1_apic1] => (item=apic/tenants) 
skipping: [fabric1_apic1] => (item=apic/tenants/vrfs) 
skipping: [fabric1_apic1] => (item=apic/tenants/bridge_domains) 
skipping: [fabric1_apic1] => (item=apic/tenants/bridge_domains/subnets) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles/endpoint_groups) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles/endpoint_groups/physical_domains) 
skipping: [fabric1_apic1] => (item=apic/tenants/application_profiles/endpoint_groups/static_ports) 
skipping: [fabric1_apic1]

TASK [process_data : Construct present_extracted_data] ***********************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [process_data : Construct absent_extracted_data] ************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

TASK [present_apic_tenants : Create/modify Tenants] **************************************************************************************************************************
changed: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'PROD'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1'})

TASK [present_apic_tenants : Create/Modify VRFs] *****************************************************************************************************************************
changed: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'PROD', 'apic/tenants/vrfs/name': 'PROD', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/enforcement_preference': 'enforced', 'apic/tenants/vrfs/preferred_group': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/vrfs/name': 'vrf-201', 'apic/tenants/vrfs/enforcement_preference': 'unenforced', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/preferred_group': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/vrfs/name': 'vrf-202', 'apic/tenants/vrfs/enforcement_preference': 'unenforced', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/preferred_group': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/vrfs/name': 'vrf-203', 'apic/tenants/vrfs/enforcement_preference': 'unenforced', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/preferred_group': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/vrfs/name': 'vrf-204', 'apic/tenants/vrfs/enforcement_preference': 'unenforced', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/preferred_group': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/vrfs/name': 'vrf-210', 'apic/tenants/vrfs/enforcement_preference': 'unenforced', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/preferred_group': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/vrfs/name': 'vrf-211', 'apic/tenants/vrfs/enforcement_preference': 'unenforced', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/preferred_group': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/vrfs/name': 'vrf-212', 'apic/tenants/vrfs/enforcement_preference': 'unenforced', 'apic/tenants/vrfs/data_plane_learning': True, 'apic/tenants/vrfs/enforcement_direction': 'ingress', 'apic/tenants/vrfs/preferred_group': False})

TASK [present_apic_tenants : Create/Modify Bridge Domains] *******************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/bridge_domains/name': 'bd-201', 'apic/tenants/bridge_domains/vrf': 'vrf-201', 'apic/tenants/bridge_domains/mac': '00:22:BD:F8:19:FF', 'apic/tenants/bridge_domains/ep_move_detection': False, 'apic/tenants/bridge_domains/arp_flooding': True, 'apic/tenants/bridge_domains/ip_dataplane_learning': True, 'apic/tenants/bridge_domains/limit_ip_learn_to_subnets': True, 'apic/tenants/bridge_domains/multi_destination_flooding': 'bd-flood', 'apic/tenants/bridge_domains/unknown_unicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv4_multicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv6_multicast': 'flood', 'apic/tenants/bridge_domains/unicast_routing': True, 'apic/tenants/bridge_domains/l3_multicast': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/bridge_domains/name': 'bd-202', 'apic/tenants/bridge_domains/vrf': 'vrf-201', 'apic/tenants/bridge_domains/mac': '00:22:BD:F8:19:FF', 'apic/tenants/bridge_domains/ep_move_detection': False, 'apic/tenants/bridge_domains/arp_flooding': True, 'apic/tenants/bridge_domains/ip_dataplane_learning': True, 'apic/tenants/bridge_domains/limit_ip_learn_to_subnets': True, 'apic/tenants/bridge_domains/multi_destination_flooding': 'bd-flood', 'apic/tenants/bridge_domains/unknown_unicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv4_multicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv6_multicast': 'flood', 'apic/tenants/bridge_domains/unicast_routing': True, 'apic/tenants/bridge_domains/l3_multicast': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/bridge_domains/name': 'bd-203', 'apic/tenants/bridge_domains/vrf': 'vrf-203', 'apic/tenants/bridge_domains/mac': '00:22:BD:F8:19:FF', 'apic/tenants/bridge_domains/ep_move_detection': False, 'apic/tenants/bridge_domains/arp_flooding': True, 'apic/tenants/bridge_domains/ip_dataplane_learning': True, 'apic/tenants/bridge_domains/limit_ip_learn_to_subnets': True, 'apic/tenants/bridge_domains/multi_destination_flooding': 'bd-flood', 'apic/tenants/bridge_domains/unknown_unicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv4_multicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv6_multicast': 'flood', 'apic/tenants/bridge_domains/unicast_routing': True, 'apic/tenants/bridge_domains/l3_multicast': False})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/bridge_domains/name': 'bd-204', 'apic/tenants/bridge_domains/vrf': 'vrf-204', 'apic/tenants/bridge_domains/mac': '00:22:BD:F8:19:FF', 'apic/tenants/bridge_domains/ep_move_detection': False, 'apic/tenants/bridge_domains/arp_flooding': True, 'apic/tenants/bridge_domains/ip_dataplane_learning': True, 'apic/tenants/bridge_domains/limit_ip_learn_to_subnets': True, 'apic/tenants/bridge_domains/multi_destination_flooding': 'bd-flood', 'apic/tenants/bridge_domains/unknown_unicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv4_multicast': 'flood', 'apic/tenants/bridge_domains/unknown_ipv6_multicast': 'flood', 'apic/tenants/bridge_domains/unicast_routing': True, 'apic/tenants/bridge_domains/l3_multicast': False})

TASK [present_apic_tenants : Create/Modify Bridge Domains Subnets] ***********************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/bridge_domains/name': 'bd-201', 'apic/tenants/bridge_domains/vrf': 'vrf-201', 'apic/tenants/bridge_domains/subnets/ip': '10.201.0.1/24', 'apic/tenants/bridge_domains/subnets/primary_ip': False, 'apic/tenants/bridge_domains/subnets/public': False, 'apic/tenants/bridge_domains/subnets/private': True, 'apic/tenants/bridge_domains/subnets/shared': False, 'apic/tenants/bridge_domains/subnets/virtual': False, 'apic/tenants/bridge_domains/subnets/no_default_gateway': False, 'apic/tenants/bridge_domains/subnets/igmp_querier': False, 'apic/tenants/bridge_domains/subnets/nd_ra_prefix': True})

TASK [present_apic_tenants : Create/Modify Application Profiles] *************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default'})

TASK [present_apic_tenants : Create/Modify Endpoint Groups] ******************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-201', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-201', 'apic/tenants/application_profiles/endpoint_groups/flood_in_encap': False, 'apic/tenants/application_profiles/endpoint_groups/intra_epg_isolation': False, 'apic/tenants/application_profiles/endpoint_groups/proxy_arp': False, 'apic/tenants/application_profiles/endpoint_groups/preferred_group': False, 'apic/tenants/application_profiles/endpoint_groups/qos_class': 'unspecified'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-202', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-202', 'apic/tenants/application_profiles/endpoint_groups/flood_in_encap': False, 'apic/tenants/application_profiles/endpoint_groups/intra_epg_isolation': False, 'apic/tenants/application_profiles/endpoint_groups/proxy_arp': False, 'apic/tenants/application_profiles/endpoint_groups/preferred_group': False, 'apic/tenants/application_profiles/endpoint_groups/qos_class': 'unspecified'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-203', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-203', 'apic/tenants/application_profiles/endpoint_groups/flood_in_encap': False, 'apic/tenants/application_profiles/endpoint_groups/intra_epg_isolation': False, 'apic/tenants/application_profiles/endpoint_groups/proxy_arp': False, 'apic/tenants/application_profiles/endpoint_groups/preferred_group': False, 'apic/tenants/application_profiles/endpoint_groups/qos_class': 'unspecified'})
ok: [fabric1_apic1 -> localhost] => (item={'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-204', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-204', 'apic/tenants/application_profiles/endpoint_groups/flood_in_encap': False, 'apic/tenants/application_profiles/endpoint_groups/intra_epg_isolation': False, 'apic/tenants/application_profiles/endpoint_groups/proxy_arp': False, 'apic/tenants/application_profiles/endpoint_groups/preferred_group': False, 'apic/tenants/application_profiles/endpoint_groups/qos_class': 'unspecified'})

TASK [present_apic_tenants : Bind EPGs to Physical Domains] ******************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item=[{'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-201', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-201', 'apic/tenants/application_profiles/endpoint_groups/physical_domains': ['phys']}, 'phys'])
ok: [fabric1_apic1 -> localhost] => (item=[{'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-202', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-202', 'apic/tenants/application_profiles/endpoint_groups/physical_domains': ['phys']}, 'phys'])
changed: [fabric1_apic1 -> localhost] => (item=[{'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-203', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-203', 'apic/tenants/application_profiles/endpoint_groups/physical_domains': ['phys-nh1-mappings']}, 'phys-nh1-mappings'])
ok: [fabric1_apic1 -> localhost] => (item=[{'apic/tenants/name': 'nh1', 'apic/tenants/application_profiles/name': 'default', 'apic/tenants/application_profiles/endpoint_groups/name': 'epg-204', 'apic/tenants/application_profiles/endpoint_groups/bridge_domain': 'bd-204', 'apic/tenants/application_profiles/endpoint_groups/physical_domains': ['phys-nh1-mappings']}, 'phys-nh1-mappings'])

TASK [present_apic_tenants : Bind Static paths to EPGs] **********************************************************************************************************************
ok: [fabric1_apic1 -> localhost] => (item={'tenant': 'nh1', 'ap': 'default', 'epg': 'epg-201', 'interface_configs': [{'encap_id': 201, 'interface': '1/19', 'leafs': [101], 'pod_id': 1, 'interface_mode': 'regular', 'deploy_immediacy': 'lazy', 'interface_type': 'switch_port'}]})
ok: [fabric1_apic1 -> localhost] => (item={'tenant': 'nh1', 'ap': 'default', 'epg': 'epg-202', 'interface_configs': [{'encap_id': 202, 'interface': '1/19', 'leafs': [101], 'pod_id': 1, 'interface_mode': 'regular', 'deploy_immediacy': 'lazy', 'interface_type': 'switch_port'}, {'encap_id': 202, 'interface': '1/19', 'leafs': [102], 'pod_id': 1, 'interface_mode': 'regular', 'deploy_immediacy': 'lazy', 'interface_type': 'switch_port'}]})

TASK [present_apic_tenants : Clean up data] **********************************************************************************************************************************
ok: [fabric1_apic1 -> localhost]

PLAY RECAP *******************************************************************************************************************************************************************
fabric1_apic1              : ok=26   changed=3    unreachable=0    failed=0    skipped=18   rescued=0    ignored=0   

duyhoan@DUYHOAN-M-6BQK ansible-aci-iac % 
```