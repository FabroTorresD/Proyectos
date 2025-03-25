import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Trabajador } from './entities/trabajador.entity';
import { TrabajadorService } from './trabajador/trabajador.service';
import { TrabajadorController } from './trabajador/trabajador.controller';
import { AreaController } from './area/area.controller';
import { Area } from './entities/area.entity';
import { AreaService } from './area/area.service';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'postgres',
      password: '1234',
      database: 'test',
      entities: [Trabajador, Area],
    }),
    TypeOrmModule.forFeature([Trabajador, Area]), 
  ],
  controllers: [AppController, TrabajadorController, AreaController],
  providers: [AppService, TrabajadorService, AreaService],
})
export class AppModule {}
