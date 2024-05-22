package org.example.controller;

import org.example.pojo.company;
import org.example.service.userService;
import org.hibernate.validator.constraints.URL;
import org.mockito.internal.util.StringUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
@RestController

public class usercontroller {
    @Autowired
    private userService userService;
    @PostMapping("/show")//注册类接口是post方法
    public List<company> companyshow(){
        List<company> cs=userService.showcompanylist();
        return cs;
    }

}
