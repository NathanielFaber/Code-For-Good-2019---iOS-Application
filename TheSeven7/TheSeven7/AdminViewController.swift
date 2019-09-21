//
//  AdminViewController.swift
//  TheSeven7
//
//  Created by Nick Pappas on 9/20/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit
import NotificationBannerSwift

class AdminViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var parentPasswordTextField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        parentPasswordTextField.delegate = self
        self.parentPasswordTextField.autocapitalizationType = .allCharacters
        if let password = UserDefaults.standard.string(forKey: "parentPassword") {
            parentPasswordTextField.placeholder = password
        }
        // Do any additional setup after loading the view.
    }
    
    @IBAction func setButtonPress(_ sender: Any) {
        //let defaults = UserDefaults.standard
        //defaults.set(parentPasswordTextField.text, forKey: "parentPassword")
        let localHost = UserDefaults.standard.string(forKey: "localhost")
        let url = URL(string: localHost! + "/parentpassword/change/" + parentPasswordTextField.text!)!
        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }
        task.resume()
        parentPasswordTextField.placeholder = parentPasswordTextField.text
        let banner = NotificationBanner(title: "Parent Password Updated", subtitle: nil, style: .success)
        banner.show()
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        
        let currentCharacterCount = textField.text?.count ?? 0
        if range.length + range.location > currentCharacterCount {
            return false
        }
        let newLength = currentCharacterCount + string.count - range.length
        return newLength <= 4
    }
    
    @IBAction func onDoneButton(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
}
