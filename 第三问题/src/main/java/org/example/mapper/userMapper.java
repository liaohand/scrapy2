package org.example.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.example.pojo.company;

import java.util.List;

@Mapper
public interface userMapper {


    @Select("select * from company")
    List<company> showcompanylist();

}
