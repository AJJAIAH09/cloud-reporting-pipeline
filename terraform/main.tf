terraform {

  required_version = ">= 1.0"

  required_providers {

    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.100"
    }

  }
}

provider "azurerm" {

  features {}

}

data "azurerm_resource_group" "existing_rg" {

  name = var.resource_group_name

}

resource "azurerm_storage_account" "storage" {

  name = var.storage_account_name

  resource_group_name = data.azurerm_resource_group.existing_rg.name

  location = data.azurerm_resource_group.existing_rg.location

  account_tier = "Standard"

  account_replication_type = "LRS"

}
resource "azurerm_virtual_network" "vnet" {

  name = "proj1-vnet"

  address_space = ["10.0.0.0/16"]

  location = data.azurerm_resource_group.existing_rg.location

  resource_group_name = data.azurerm_resource_group.existing_rg.name

}

resource "azurerm_subnet" "subnet" {

  name = "proj1-subnet"

  resource_group_name = data.azurerm_resource_group.existing_rg.name

  virtual_network_name = azurerm_virtual_network.vnet.name

  address_prefixes = ["10.0.1.0/24"]

}

resource "azurerm_public_ip" "public_ip" {

  name = "proj1-pip"

  location = data.azurerm_resource_group.existing_rg.location

  resource_group_name = data.azurerm_resource_group.existing_rg.name

  allocation_method = "Static"

}

resource "azurerm_network_interface" "nic" {

  name = "proj1-nic"

  location = data.azurerm_resource_group.existing_rg.location

  resource_group_name = data.azurerm_resource_group.existing_rg.name

  ip_configuration {

    name = "internal"

    subnet_id = azurerm_subnet.subnet.id

    private_ip_address_allocation = "Dynamic"

    public_ip_address_id = azurerm_public_ip.public_ip.id

  }

}
