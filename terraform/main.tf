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
