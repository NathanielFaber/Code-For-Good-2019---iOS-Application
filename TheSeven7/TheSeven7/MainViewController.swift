//
//  ViewController.swift
//  TheSeven7
//
//  Created by Ayline Villegas  on 9/20/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit

class MainViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        UserDefaults.standard.set("1234", forKey: "adminPassword")
        // Do any additional setup after loading the view.
    }


}

