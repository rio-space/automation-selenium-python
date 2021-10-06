btn_upload = "//div[@id='cv']//label[contains(@class,'DefaultButton')]"
dlg_upload = "//div[@data-test-id='upload-dialog']"
chk_prefill_on = "//label[contains(normalize-space(),'Profile prefill is on')]//ancestor::div[" \
                 "@data-test-id='upload-dialog'] "
btn_prefill = "//div[@data-test-id='upload-dialog']//input[@type='checkbox']"
sts_bar_upload = "//small[normalize-space(text())='Uploading...']//parent::div[contains(@class, 'StatusContent')]"
msg_upload_prefill_success = "//div[@data-test-id='upload-dialog']//p[text()='Your CV has been uploaded, and your profile " \
                        "has been prefilled!']"
msg_upload_no_prefill_success = "//div[@data-test-id='upload-dialog']//p[text()='Success, your CV has been uploaded!']"
btn_cancel = "//*[name() = 'svg'][contains(@class,'CloseIconButton')]"
msg_es_needs_review = "//h3[text()='Experience and Skills']//span[contains(normalize-space(),'Needs review')]"
btn_edit = "//h3[text()='Experience and Skills']//parent::div//a[text()='Edit']"
btn_delete = "//*[name() = 'svg']//parent::i[contains(@class,'StyledTrashIcon')]"
lnk_download_file = "//div[contains(@class,'StatusContent')]//a[@download]"
dt_upload = "//div[contains(@class,'StatusContent')]//small[contains(@class,'DateText')]"

