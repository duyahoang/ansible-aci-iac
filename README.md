# Ansible-ACI-IaC Solution

An Infrastructure as Code (IaC) solution to automate the deployment and configuration of Cisco ACI using [Ansible ACI collection](https://galaxy.ansible.com/ui/repo/published/cisco/aci/).
The ACI data model is based on the official [Cisco ACI Data Model](https://developer.cisco.com/docs/nexus-as-code/#!data-model)

An Ansible Infrastructure as Code (IaC) solution is designed to automate Cisco ACI (Application Centric Infrastructure) deployment configurations using data models and custom Jinja2 filters. The solution leverages native [Cisco ACI Ansible modules](https://galaxy.ansible.com/ui/repo/published/cisco/aci/) to push configurations to the ACI fabric, ensuring compatibility and support with Cisco's offerings. By abstracting configurations into central structured data models, the solution enhances clarity, manageability, and ensures consistency across multiple ACI deployments. The ACI data model is based on the official [Cisco ACI Data Model](https://developer.cisco.com/docs/nexus-as-code/#!data-model)
 
## Features

- **Data-Driven Design**: Utilizes YAML-based data models to clearly and concisely represent complex ACI configurations.
- **Native Cisco ACI Support**: Uses native Cisco ACI Ansible modules, thereby supporting union features between Cisco ACI Ansible modules and ACI Data Model offers. The solution also supports `--check` mode as the Cisco ACI Ansible modules support it.
- **Modular Design**: Organized into extendable roles and tasks, allowing for focused configurations
  -  Roles: `present_apic_tenants` and `present_apic_access_policies`.
  -  Roles are still in development to completely and fully support the ACI Data Model. At this moment the solution is to serve as a beta testing version.
- **Custom Filters**: A suite of custom Jinja2 filters to transform, extract, and process the data models for various use cases.
- **Scalability**: Designed to manage configurations for any size of ACI environments, from small setups to large enterprise deployments.
- **Idempotency**: Guarantees consistent configurations across runs, avoiding unnecessary changes if the desired state is already achieved.
- **Differential Analysis**: Identifies and acts upon differences between data in `previous_data_directory` and `data_directory`. If `previous_data_directory` is provided in `vars/hosts.yaml`, the solution will only run ACI modules against the different configurations.
- **Defaults Inclusion**: Integrates default values from `defaults.yaml` into the data configurations, ensuring a base configuration state.
- **Error Handling and Logging**: Comprehensive error handling with detailed logs maintained in `ansible.log`.

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

## Usage

1. **Configure Environment Variables**: Go to `vars/hosts.yaml` and update with your ACI environment details, including login credentials and common parameters for Cisco ACI modules. If `previous_data_directory` is provided, it will trigger the comparison and only run ACI modules against the different objects.

2. **Data Models**: Populate the data models in the `data` directory with your desired ACI configurations. This is where you define your ACI fabric's desired state. Make sure to include the path to data configuration in `vars/hosts.yaml` with the parameter `data_directory`. 

3. **Playbook's Hosts**: Update the `hosts` in the `config_apic.yaml` playbook to reflect the fabric you want to run.
 
5. **Deploy configurations**: Navigate to the root directory of the solution and execute the `config_apic.yaml` playbook:
   With `check` mode
   ```bash
   ansible-playbook playbooks/config_apic.yaml --check --verbose
   ```
   Run playbook
   ```bash
   ansible-playbook playbooks/config_apic.yaml
   ```

## Limitations

- Password-based authentication requires a separate login request and an open session for each module execution. More on the official [Cisco ACI Ansible Guide](https://docs.ansible.com/ansible/latest/scenario_guides/guide_aci.html#password-based-authentication).

## Warning

Utilizing password-based authentication frequently or in rapid succession may lead to triggering ACI's anti-DoS measures. This can result in session throttling and cause HTTP 503 errors and login failures. It is advisable to use this method judiciously and be aware of the potential repercussions. More on the official [Cisco ACI Ansible Guide](https://docs.ansible.com/ansible/latest/scenario_guides/guide_aci.html#password-based-authentication).

## Example

The `example-playbook-execution,txt` file show the example of execute playbook and its output.

## Author
Duy Hoang
duyhoan@cisco.com

---
