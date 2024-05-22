package org.example.service.impl;

import org.example.mapper.userMapper;
import org.example.pojo.company;
import org.example.service.userService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class userServiceImpl implements userService {
    @Autowired
    private userMapper usermapper;

    @Override
    public List<company> showcompanylist() {
        return usermapper.showcompanylist();
    }

}
