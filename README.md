# Ansible-ACI-IaC Solution

An Infrastructure as Code (IaC) solution to automate the deployment and configuration of Cisco ACI using [Ansible ACI collection](https://galaxy.ansible.com/ui/repo/published/cisco/aci/).
The ACI data model is based on the official [Cisco ACI Data Model](https://developer.cisco.com/docs/nexus-as-code/#!data-model)
 
## Requirements

- **Ansible-Core**: This solution is built on `ansible-core`. Follow the latest recommended `ansible-core` version from the official [Ansible ACI collection](https://galaxy.ansible.com/ui/repo/published/cisco/aci/) website.
  ```bash
  pip install ansible-core
  ```
  
- **Ansible ACI Collection**: Ensure you have the required Ansible ACI collection. Follow the latest recommended Ansible ACI collection version from the official [Ansible ACI collection](https://galaxy.ansible.com/ui/repo/published/cisco/aci/) website. Install it with:
  ```bash
  ansible-galaxy collection install cisco.aci
  ```
  
- **Python**: Version `3.7` or above is required. Install it with:
  ```bash
  pip install 'python>=3.7'
  ```

## Installation

1. **Make sure all the Requirements are installed**:
   
2. **Cloning and Setting up Ansible-ACI-IaC**:

   - Clone the repository:
     ```bash
     git clone https://github.com/duyahoang/ansible-aci-iac.git
     ```

   - Navigate to the cloned directory:
     ```bash
     cd ansible-aci-iac
     ```

## Features

- **Modular Design**: Easily extendable roles and tasks to fit specific requirements.
  
- **Custom Filters**: Includes custom filters like `extractor` for enhanced data parsing and manipulation.
  
- **Scalability**: Designed to manage configurations for any size of ACI environments, from small setups to large enterprise deployments.
  
- **Idempotent**: Ensures desired state configuration, making repeated runs safe.

## Usage

1. **Configure Environment Variables**: Set up necessary variables like APIC credentials in the `group_vars` or `host_vars` directories.

2. **Update Configuration**: Modify `vars/host_vars/apic1/apic_configuration.yaml` with your specific ACI configurations.

3. **Run Playbook**: Deploy configurations to your ACI environment:
   ```bash
   ansible-playbook playbooks/config_apic.yaml
   ```

## Example

Given a simple configuration in `vars/host_vars/apic1/apic_configuration.yaml`:

```yaml
apic:
  tenants:
    - name: PROD
      vrfs:
        - name: PROD
```

Run the playbook:

```bash
ansible-playbook playbooks/config_apic.yaml
```

Output:
```bash
PLAY [Deploy APIC configuration] ****************************************************************************************************************************************************************************************************************************************************************************

TASK [present_apic : Create Tenants] ************************************************************************************************************************************************************************************************************************************************************************
changed: [apic1 -> localhost] => (item={'apic_tenants_name': 'PROD'}) => changed=true 
  ansible_loop_var: item
  current: []
  item:
    apic_tenants_name: PROD
  mo:
    fvTenant:
      attributes:
        annotation: orchestrator:ansible
        dn: uni/tn-PROD
        name: PROD

TASK [present_apic : Create VRFs] ***************************************************************************************************************************************************************************************************************************************************************************
changed: [apic1 -> localhost] => (item={'apic_tenants_name': 'PROD', 'apic_tenants_vrfs_name': 'PROD'}) => changed=true 
  ansible_loop_var: item
  current: []
  item:
    apic_tenants_name: PROD
    apic_tenants_vrfs_name: PROD
  mo:
    fvCtx:
      attributes:
        annotation: orchestrator:ansible
        dn: uni/tn-PROD/ctx-PROD
        name: PROD

TASK [present_apic : Create Bridge Domains] *****************************************************************************************************************************************************************************************************************************************************************
skipping: [apic1] => changed=false 
  skipped_reason: No items in the list

PLAY RECAP **************************************************************************************************************************************************************************************************************************************************************************************************
apic1                      : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```

This will ensure that the tenant named "PROD" with a VRF also named "PROD" is present in the ACI environment.

## Author
Duy Hoang
duyhoan@cisco.com

---
