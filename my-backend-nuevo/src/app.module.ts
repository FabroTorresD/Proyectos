import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Trabajador } from './entities/trabajador.entity';
import { TrabajadorService } from './trabajador/trabajador.service';
import { TrabajadorController } from './trabajador/trabajador.controller';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'postgres',
      password: '1234',
      database: 'test',
      entities: [Trabajador],
      synchronize: true, // Solo para desarrollo
    }),
    TypeOrmModule.forFeature([Trabajador]), 
  ],
  controllers: [AppController, TrabajadorController],
  providers: [AppService, TrabajadorService],
})
export class AppModule {}
