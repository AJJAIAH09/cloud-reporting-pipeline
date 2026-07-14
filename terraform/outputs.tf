output "resource_group_name" {

  value = data.azurerm_resource_group.existing_rg.name

}

output "storage_account_name" {

  value = azurerm_storage_account.storage.name

}

output "storage_account_id" {

  value = azurerm_storage_account.storage.id

}
