//
//  AdminLoginViewController.swift
//  TheSeven7
//
//  Created by Nick Pappas on 9/21/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit

class AdminLoginViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var adminTextField: UITextField!
    
    let password = UserDefaults.standard.string(forKey: "adminPassword")
    
    override func viewDidLoad() {
        super.viewDidLoad()
        adminTextField.delegate = self
        self.adminTextField.autocapitalizationType = .allCharacters
        adminTextField.addTarget(self, action: #selector(AdminLoginViewController.textFieldDidChange(_:)), for: UIControl.Event.editingChanged)
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        
        let currentCharacterCount = textField.text?.count ?? 0
        if range.length + range.location > currentCharacterCount {
            return false
        }
        let newLength = currentCharacterCount + string.count - range.length
        return newLength <= 4
    }
    
    @objc func textFieldDidChange(_ textField: UITextField) {
        if (adminTextField.text == password) {
            adminTextField.text = ""
            performSegue(withIdentifier: "adminPassword", sender: self)
            adminTextField.resignFirstResponder()
        }
    }
}
